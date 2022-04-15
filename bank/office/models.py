from django.db import models
from main_page.models import User, Account, Transfer, Installment


class EnterpriseSpecialist(User):
    def create(self):
        ko = 1


class Operator(User):
    operations = models.ManyToManyField(Transfer)

    def get_new_operation(self, new_operation):
        self.operations.add(new_operation)

    def cancel_operation(self, transfer):
        if transfer.name == 'transfer':
            from_acc = transfer.accounts.all()[0]
            from_acc.add_money(transfer.money)
            from_acc.save()
            to_acc = transfer.accounts.all()[1]
            to_acc.get_money(transfer.money)
            to_acc.save()
        if transfer.name == 'refill':
            to_acc = transfer.accounts.all()[0]
            to_acc.get_money(transfer.money)
            to_acc.save()
        self.operations.remove(transfer)
        transfer.delete()


class Manager(Operator):
    not_approved_accounts = models.ManyToManyField(Account)
    not_approved_installments = models.ManyToManyField(Installment)

    def get_new_request_on_registration(self, new_accounts):
        self.not_approved_accounts.add(new_accounts)

    def approve_account(self, acc):
        acc.approved = True
        acc.save()
        self.not_approved_accounts.remove(acc)

    def refuse_account(self, acc):
        acc.delete()
        self.not_approved_accounts.remove(acc)

    def get_new_request_on_installments(self, new_installment):
        self.not_approved_installments.add(new_installment)

    def approve_installment(self, installment):
        installment.approved = True
        installment.save()
        self.not_approved_installments.remove(installment)

    def refuse_installment(self, installment):
        installment.delete()
        self.not_approved_installments.remove(installment)

