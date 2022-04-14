from .models import Bank, Account, User, Transfer
from django import forms
from django.forms import ModelForm, RadioSelect, TextInput, NumberInput


class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['juridical_name']
        banks = Bank.objects.all()
        k = 1
        CHOISE = []
        for bank in banks:
            CHOISE.append((k, bank.juridical_name))
            k += 1
        widgets = {
            'juridical_name': RadioSelect(choices=CHOISE, attrs={
                'placeholder': "Bank"
            })
        }


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['number']
        widgets = {
            'number': NumberInput(attrs={
                'placeholder': "Account"
            })
        }


class MoneyForm(ModelForm):
    class Meta:
        model = Account
        fields = ['money']
        widgets = {
            'money': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Summa",
            })
        }