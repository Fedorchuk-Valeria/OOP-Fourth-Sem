from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm, UserForm
from main_page.models import User
import main_page.views
import main_page.forms


class FirstPageController(View):

    def get(self, request):
        current_u = User()
        try:
            current_u = User.objects.filter(online=True)
            for c_u in current_u:
                c_u.online = False
                c_u.save()
        except current_u.DoesNotExist:
            current_u = None
        return render(request, 'first_page/choose.html')


class SignUpController(View):

    def get(self, request):
        form = NewUserForm()
        return render(request, 'first_page/sign_up.html', {'form': form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sign_in')


class SignInController(View):

    profile_template = 'main_page/profile.html'
    start_template = 'first_page/log_in.html'
    model = User

    def get(self, request):
        current_u = self.model()
        try:
            current_u = self.model.objects.filter(online=True)
            for c_u in current_u:
                c_u.online = False
                c_u.save()
        except current_u.DoesNotExist:
            current_u = None
        error_message = ''
        form = UserForm()
        f_d = {
            'form': form,
            'error': error_message
        }
        return render(request, self.start_template, f_d)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = self.model()
        try:
            user = self.model.objects.get(email=email, password=password)
            d = {'user': user}
            user.online = True
            user.save()
            return render(request, self.profile_template, d)
        except user.DoesNotExist:
            error_message = 'User not found'
            form = UserForm()
            f_d = {
                'form': form,
                'error': error_message
            }
            return render(request, self.start_template, f_d)


class ProfileController(View):

    profile_template = 'main_page/profile.html'
    start_template = 'first_page/log_in.html'
    model = User

    def get(self, request):
        current_user = self.model()
        try:
            current_user = self.model.objects.get(online=True)
        except current_user.DoesNotExist:
            current_user = None
        if current_user:
            d = {'user': current_user}
            return render(request, self.profile_template, d)
