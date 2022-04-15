from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User, Bank, Account, Transfer, Credit, Installment
from .forms import BankForm, AccountForm, MoneyForm, InstallmentForm
from first_page.forms import UserForm
from django.views import View
from office.models import Manager, Operator


class AccountsController(viewsets.ViewSet):

    def get_one_acc(self, request):
        current_acc = Account()
        try:
            current_acc = Account.objects.get(current=True)
        except current_acc.DoesNotExist:
            current_acc = None
        return render(request, 'main_page/account.html', {'account': current_acc})

    def get(self, request):
        current_acc = Account()
        try:
            current_acc = Account.objects.filter(current=True)
            for c_a in current_acc:
                c_a.current = False
                c_a.save()
        except current_acc.DoesNotExist:
            current_acc = None
        u = User()
        try:
            u = User.objects.get(online=True)
        except u.DoesNotExist:
            u = None
        accounts = u.account_set.all().filter(approved=True)
        form = AccountForm()
        d = {'form': form,
             'user': u,
             'accounts': accounts
             }
        return render(request, 'main_page/accounts.html', d)

    def post(self, request):
        i = int(request.POST.get('number')) - 1
        u = User()
        try:
            u = User.objects.get(online=True)
        except u.DoesNotExist:
            u = None
        accounts = u.account_set.all().filter(approved=True)
        acc = accounts[i]
        acc.current = True
        acc.save()
        return render(request, 'main_page/account.html', {'account': acc})

    def get_new_acc(self, request):
        mess = ''
        form = BankForm()
        return render(request, 'main_page/new_account.html', {'form': form, 'message': mess})

    def post_new_acc(self, request):
        i = int(request.POST.get('juridical_name'))
        name = BankForm.Meta.CHOISE[i - 1][1]
        bank = Bank.objects.get(juridical_name=name)
        user = User()
        try:
            user = User.objects.get(online=True)
        except user.DoesNotExist:
            user = None
        b_account = Account()
        b_account.create(bank, user)
        b_account.save()
        manager = Manager.objects.get(work_place=bank)
        manager.get_new_request_on_registration(b_account)
        manager.save()
        mess = 'Send for check'
        form = BankForm()
        return render(request, 'main_page/new_account.html', {'form': form, 'message': mess})

    def get_put_money(self, request):
        message = ''
        form = MoneyForm()
        return render(request, 'main_page/refill.html', {'form': form, 'message': message})

    def post_put_money(self, request):
        count_of_money = int(request.POST.get('money'))
        curr_acc = Account.objects.get(current=True)
        bank = curr_acc.bank
        operators = Operator.objects.filter(work_place=bank)
        operator = Operator()
        for op in operators:
            if not isinstance(op, Manager):
                operator = op
        t = Transfer()
        t.save()
        message = t.put_money(curr_acc, count_of_money)
        t.save()
        operator.get_new_operation(t)
        operator.save()
        curr_acc.save()
        form = MoneyForm()
        return render(request, 'main_page/refill.html', {'form': form, 'message': message})

    def get_get_money(self, request):
        message = ''
        form = MoneyForm()
        return render(request, 'main_page/withdrawal.html', {'form': form, 'message': message})

    def post_get_money(self, request):
        count_of_money = int(request.POST.get('money'))
        curr_acc = Account.objects.get(current=True)
        bank = curr_acc.bank
        operators = Operator.objects.filter(work_place=bank)
        operator = Operator()
        for op in operators:
            if not isinstance(op, Manager):
                operator = op
        t = Transfer()
        t.save()
        message = t.withdraw_money(curr_acc, count_of_money)
        t.save()
        operator.get_new_operation(t)
        operator.save()
        curr_acc.save()
        form = MoneyForm()
        return render(request, 'main_page/withdrawal.html', {'form': form, 'message': message})

    def get_money_transfer(self, request):
        message = ''
        curr_acc = Account.objects.get(current=True)
        m_form = MoneyForm()
        acc_form = AccountForm()
        d = {
            'current': curr_acc,
            'm_form': m_form,
            'acc_form': acc_form,
            'message': message
        }
        return render(request, 'main_page/transfer.html', d)

    def post_money_transfer(self, request):
        message = ''
        curr_acc = Account.objects.get(current=True)
        count_of_money = int(request.POST.get('money'))
        to_acc = Account()
        try:
            to_acc = Account.objects.get(number=request.POST.get('number'))
            bank = curr_acc.bank
            operators = Operator.objects.filter(work_place=bank)
            operator = Operator()
            for op in operators:
                if not isinstance(op, Manager):
                    operator = op
            t = Transfer()
            t.save()
            message = t.transfer_to_another_account(curr_acc, to_acc, count_of_money)
            t.save()
            operator.get_new_operation(t)
            operator.save()
            curr_acc.save()
            to_acc.save()
        except to_acc.DoesNotExist:
            to_acc = None
            message = 'To: error, not found'
        m_form = MoneyForm()
        acc_form = AccountForm()
        d = {
            'current': curr_acc,
            'm_form': m_form,
            'acc_form': acc_form,
            'message': message
        }
        return render(request, 'main_page/transfer.html', d)

    def get_freeze(self, request):
        curr_acc = Account.objects.get(current=True)
        mess = curr_acc.un_freeze()
        curr_acc.save()
        return render(request, 'main_page/account.html', {'account': curr_acc, 'message': mess})

    def get_bloke(self, request):
        curr_acc = Account.objects.get(current=True)
        curr_acc.delete()
        return redirect('my_accounts')


class InstallmentsController(viewsets.ViewSet):

    def get(self, request):
        current_inst = Installment()
        try:
            current_inst = Installment.objects.filter(current=True)
            for c_i in current_inst:
                c_i.current = False
                c_i.save()
        except current_inst.DoesNotExist:
            current_inst = None
        u = User()
        try:
            u = User.objects.get(online=True)
        except u.DoesNotExist:
            u = None
        installments = u.installment_set.all().filter(approved=True)
        for item in installments:
            if isinstance(item, Credit):
                installments.remove(item)
        #credits = u.credit_set.all().filter(approved=True)
        form = AccountForm()
        d = {'form': form,
             'user': u,
             'installments': installments
             }
        return render(request, 'main_page/installments.html', d)

    def get_create_installment(self, request):
        form = InstallmentForm()
        return render(request, 'main_page/new_installment.html', {'form': form})

    def post_create_installment(self, request):
        i = request.POST.get('bank')
        bank = Bank.objects.get(id=i)
        i = int(request.POST.get('count_of_month'))
        month = InstallmentForm.Meta.CHOISE_MONTH[i - 1][1]
        money = request.POST.get('count_of_money')
        user = User()
        try:
            user = User.objects.get(online=True)
        except user.DoesNotExist:
            user = None
        installment = Installment()
        installment.create(user, bank, money, month)
        installment.save()
        manager = Manager()
        manager = Manager.objects.get(work_place=bank)
        manager.get_new_request_on_installments(installment)
        manager.save()
        mess = 'Send for check'
        form = InstallmentForm()
        return render(request, 'main_page/new_installment.html', {'form': form, 'message': mess})


class CreditsController(View):

    def get(self, request):
        current_cr = Credit()
        try:
            current_inst = Credit.objects.filter(current=True)
            for c_i in current_inst:
                c_i.current = False
                c_i.save()
        except current_inst.DoesNotExist:
            current_inst = None
        u = User()
        try:
            u = User.objects.get(online=True)
        except u.DoesNotExist:
            u = None
        credits = []
        installments = u.installment_set.all().filter(approved=True)
        for item in installments:
            if isinstance(item, Credit):
                credits.append(item)
        form = AccountForm()
        d = {'form': form,
             'user': u,
             'credits': credits
             }
        return render(request, 'main_page/credits.html', d)



