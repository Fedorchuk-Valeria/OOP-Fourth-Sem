from django.urls import path
from . import views
from .views import RequestsController, OperationsController, RequestsInstallmentsController
from first_page.views import ProfileController, SignInController
from .models import Manager, Operator

urlpatterns = [
    path('start/manager', SignInController.as_view(profile_template='office/profile_manager.html',
                                                    start_template='office/sign_in.html',
                                                    model=Manager), name='start_manager'),
    path('home/manager', ProfileController.as_view(profile_template='office/profile_manager.html',
                                                   start_template='office/sign_in.html',
                                                   model=Manager), name='profile_manager'),
    path('manager/reg/requests', RequestsController.as_view(), name='reg_requests'),
    #path('manager/reg/request', RequestsController.as_view(), name='reg_request')
    path('start/operator', SignInController.as_view(profile_template='office/profile_operator.html',
                                                    start_template='office/sign_in_operator.html',
                                                    model=Operator), name='start_operator'),
    path('home/operator', ProfileController.as_view(profile_template='office/profile_operator.html',
                                                    start_template='office/sign_in_operator.html',
                                                    model=Operator), name='profile_operator'),
    path('operator/transfer/operations', OperationsController.as_view(), name='transfer_operations'),
    path('manager/installments/requests', RequestsInstallmentsController.as_view(), name='installments_requests')
]