from django.shortcuts import render, redirect
from django.views import View
from first_page.forms import UserForm
from main_page.models import Account, Transfer
from main_page.forms import AccountForm
from .models import Manager, Operator
from .forms import IndexForm


# def sign_in_manager(request):
#     current_m = Manager()
#     try:
#         current_m = Manager.objects.filter(online=True)
#         for c_m in current_m:
#             c_m.online = False
#             c_m.save()
#     except current_m.DoesNotExist:
#         current_m = None
#     error_message = ''
#     if request.method == 'POST':
#         return get_manager_profile(request)
#     form = UserForm()
#     f_d = {
#         'form': form,
#         'error': error_message
#     }
#     return render(request, 'office/sign_in.html', f_d)


# def get_manager_profile(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     mess = ''
#     current_manager = Manager()
#     try:
#         current_manager = Manager.objects.get(online=True)
#     except current_manager.DoesNotExist:
#         current_manager = None
#     if current_manager:
#         return render(request, 'office/profile_manager.html', {'manager': current_manager})
#     current_manager = Manager()
#     try:
#         current_manager = Manager.objects.get(email=email, password=password)
#     except current_manager.DoesNotExist:
#         current_manager = None
#     if current_manager:
#         current_manager.online = True
#         current_manager.save()
#         return render(request, 'office/profile_manager.html', {'manager': current_manager})
#     else:
#         mess = 'User not found'
#     form = UserForm()
#     return render(request, 'office/sign_in.html', {'form': form, 'error': mess})


class RequestsController(View):
    form = AccountForm()

    def get(self, request):
        m = Manager()
        try:
            m = Manager.objects.get(online=True)
        except m.DoesNotExist:
            m = None
        if m.not_approved_accounts:
            accounts = m.not_approved_accounts.all()
        else:
            accounts = []
        d = {'form': self.form,
             'manager': m,
             'accounts': accounts
             }
        return render(request, 'office/requests.html', d)

    def post(self, request):
        m = Manager()
        try:
            m = Manager.objects.get(online=True)
        except m.DoesNotExist:
            m = None
        if request.POST.get('number'):
            i = int(request.POST.get('number')) - 1
            acc = m.not_approved_accounts.all()[i]
            acc.current = True
            acc.save()
            return render(request, 'office/request.html', {'acc': acc})
        acc = Account()
        try:
            acc = Account.objects.get(current=True)
        except acc.DoesNotExist:
            acc = None
        if request.POST.get('btn') == 'Approve':
            m.approve(acc)
            m.save()
        else:
            m.refuse(acc)
            m.save()
        accounts = m.not_approved_accounts.all()
        d = {'form': self.form,
             'manager': m,
             'accounts': accounts
        }
        return render(request, 'office/requests.html', d)


class OperationsController(View):

    def get(self, request):
        form = IndexForm()
        op = Operator()
        try:
            op = Operator.objects.get(online=True)
        except op.DoesNotExist:
            op = None
        information = []
        if op.operations:
            operations = op.operations.all()
            for o in operations:
                name = o.name
                from_acc = ''
                to_acc = ''
                if name == 'transfer':
                    from_acc = o.accounts.all()[0]
                    to_acc = o.accounts.all()[1]
                if name == 'refill':
                    to_acc = o.accounts.all()[0]
                if name == 'withdrawal':
                    from_acc = o.accounts.all()[0]
                c = {'name': name, 'from': from_acc, 'to': to_acc, 'money': o.money}
                information.append(c)
        d = {'form': form,
             'operator': op,
             'operations': information
             }
        return render(request, 'office/transfer_operations.html', d)

    def post(self, request):
        op = Operator()
        try:
            op = Operator.objects.get(online=True)
        except op.DoesNotExist:
            op = None
        if request.POST.get('choose'):
            i = int(request.POST.get('choose')) - 1
            t = op.operations.all()[i]
            t.chosen = True
            t.save()
            name = t.name
            from_acc = ''
            to_acc = ''
            if t.name == 'transfer':
                from_acc = t.accounts.all()[0]
                to_acc = t.accounts.all()[1]
            if t.name == 'refill':
                to_acc = t.accounts.all()[0]
            if t.name == 'withdrawal':
                from_acc = t.accounts.all()[0]
            c = {'name': name, 'from': from_acc, 'to': to_acc, 'money': t.money}
            return render(request, 'office/transfer.html', {'transfer': c})
        t = Transfer()
        try:
            t = Transfer.objects.get(chosen=True)
        except t.DoesNotExist:
            t = None
        if request.POST.get('btn') == 'Cancel':
            op.cancel_operation(t)
        information = []
        if op.operations:
            operations = op.operations.all()
            for o in operations:
                name = o.name
                from_acc = ''
                to_acc = ''
                if name == 'transfer':
                    from_acc = o.accounts.all()[0]
                    to_acc = o.accounts.all()[1]
                if name == 'refill':
                    to_acc = o.accounts.all()[0]
                if name == 'withdrawal':
                    from_acc = o.accounts.all()[0]
                c = {'name': name, 'from': from_acc, 'to': to_acc, 'money': o.money}
                information.append(c)
        form = IndexForm()
        d = {'form': form,
             'operator': op,
             'operations': information
             }
        return render(request, 'office/transfer_operations.html')

