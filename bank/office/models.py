from django.db import models
from main_page.models import User, Account, Transfer


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

    def get_new_request_on_registration(self, new_accounts):
        self.not_approved_accounts.add(new_accounts)

    def approve(self, acc):
        acc.approved = True
        acc.save()
        self.not_approved_accounts.remove(acc)

    def refuse(self, acc):
        acc.delete()
        self.not_approved_accounts.remove(acc)


