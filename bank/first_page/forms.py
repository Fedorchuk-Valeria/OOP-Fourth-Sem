from main_page.models import User
from django.forms import ModelForm, TextInput, SelectDateWidget


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'date_of_birth', 'phone_number', 'identification_number', 'passport_number',
                  'email', 'password']
        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Full name",
            }),
            "date_of_birth":  SelectDateWidget(years=range(1950, 2004), attrs={
                'class': "form-control",
                'placeholder': "Date of birth",
            }),
            "passport_number": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Passport number",
            }),
            "identification_number": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Identification number",
            }),
            "phone_number": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Phone number",
            }),
            "email": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Email address",
            }),
            "password": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Password",
            })
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            "email": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Email address",
            }),
            "password": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Password",
            })
        }
