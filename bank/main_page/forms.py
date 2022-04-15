from .models import Bank, Account, User, Transfer, Installment
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
            'money': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Summa",
            })
        }


class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ['bank', 'count_of_money', 'count_of_month']
        banks = Bank.objects.all()
        k = 1
        CHOISE_BANK = []
        for bank in banks:
            CHOISE_BANK.append((k, bank.juridical_name))
            k += 1
        CHOISE_MONTH = [('1', '3'), ('2', '6'), ('3', '12'), ('4', '24'), ('5', '36')]
        widgets = {
            'bank': RadioSelect(choices=CHOISE_BANK, attrs={
                'placeholder': "Bank"
            }),
            'count_of_month': RadioSelect(choices=CHOISE_MONTH, attrs={
                'placeholder': "Month"
            }),
            'count_of_money': NumberInput(attrs={
                'placeholder': "Summa",
            })
        }
