from django.urls import path
from .views import FirstPageController, SignUpController, ProfileController, SignInController

urlpatterns = [
    path('', FirstPageController.as_view(), name='beginning'),
    path('start/client', SignInController.as_view(profile_template='main_page/profile.html',
                                                  start_template='first_page/log_in.html'), name='sign_in'),
    path('start', SignUpController.as_view(), name='sign_up')
]