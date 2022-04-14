from django.db import models
import random
from datetime import datetime


class Enterprise(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    type = models.CharField(max_length=20, null=True)
    juridical_name = models.CharField(max_length=40, null=True)
    payer_account_number = models.CharField(max_length=10, null=True)
    bank_id = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=40, null=True)
    workers = None

    def __str__(self):
        return self.juridical_name


class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    date_of_birth = models.DateField(auto_now=False, null=True)
    passport_number = models.CharField(primary_key=True, max_length=30, default='')
    identification_number = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=30, null=True)
    password = models.CharField(max_length=15, null=True)
    work_place = models.ForeignKey(Enterprise, on_delete=models.SET_NULL, null=True)
    online = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    def registration(self, name, date, passport_number, identification_number, phone, email, password):
        self.name = name
        self.date_of_birth = date
        self.passport_number = passport_number
        self.identification_number = identification_number
        self.phone_number = phone
        self.email = email
        self.password = password


class Bank(Enterprise):
    def re(self):
        l=1


class Account(models.Model):
    frozen = models.BooleanField(default=False)
    money = models.IntegerField(null=True)
    date_of_creation = models.DateField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    number = models.CharField(primary_key=True, max_length=10, default='-1')
    current = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return str(self.number + ' ' + self.user.name)
        return ''

    def create(self, bank, user):
        self.money = 0
        number = str(random.random())
        self.number = number.replace('.', '')[:10]
        self.bank = bank
        self.user = user
        self.date_of_creation = datetime.now()

    def add_money(self, summa):
        if not self.frozen:
            self.money += summa
            return 'Ok'
        return 'Account is frozen'

    def get_money(self, summa):
        if self.frozen:
            return 'Account is frozen'
        elif summa <= self.money:
            self.money -= summa
            return 'Ok'
        else:
            return 'Not enough money!'

    def un_freeze(self):
        if self.frozen:
            self.frozen = False
            return 'Account is unfrozen'
        else:
            self.frozen = True
            return 'Account is frozen'


class Transfer(models.Model):
    name = models.CharField(max_length=30, null=True)
    accounts = models.ManyToManyField(Account)
    money = models.IntegerField(null=True)
    chosen = models.BooleanField(default=False)

    def transfer_to_another_account(self, from_acc, to_acc, money):
        self.name = 'transfer'
        self.accounts.add(from_acc)
        self.accounts.add(to_acc)
        self.money = money
        mess1 = from_acc.get_money(self.money)
        mess2 = to_acc.add_money(self.money)
        if mess1 == mess2:
            return mess1
        return mess1 + mess2

    def put_money(self, to_acc, money):
        self.name = 'refill'
        self.accounts.add(to_acc)
        self.money = money
        mess = to_acc.add_money(self.money)
        return mess

    def withdraw_money(self, from_acc, money):
        self.name = 'withdrawal'
        self.accounts.add(from_acc)
        self.money = money
        mess = from_acc.get_money(self.money)
        return mess


class Installment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    count_of_money = models.IntegerField(null=True)
    count_of_month = models.IntegerField(null=True)
    current = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)


class Credit(Installment):
    percent = models.IntegerField(null=True)

