from django import forms


class AnswerForm(forms.Form):
    btn = forms.CharField()


class IndexForm(forms.Form):
    choose = forms.IntegerField(widget=forms.NumberInput())
