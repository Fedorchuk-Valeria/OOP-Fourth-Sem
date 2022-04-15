from django.urls import path
from first_page.views import ProfileController
from .views import AccountsController, InstallmentsController, CreditsController

urlpatterns = [
    path('', ProfileController.as_view(profile_template='main_page/profile.html',
                                       start_template='first_page/log_in.html'), name='profile'),
    path('accounts', AccountsController.as_view({'get': 'get'}), name='my_accounts'),
    path('add/accounts', AccountsController.as_view({'get': 'get_new_acc', 'post': 'post_new_acc'}),
         name='new_account'),
    path('change/account', AccountsController.as_view({'get': 'get_one_acc'}),
         name='account'),
    path('account/put', AccountsController.as_view({'get': 'get_put_money', 'post': 'post_put_money'}),
         name='put_money'),
    path('account/get', AccountsController.as_view({'get': 'get_get_money', 'post': 'post_get_money'}),
         name='get_money'),
    path('account/transfer', AccountsController.as_view({'get': 'get_money_transfer', 'post': 'post_money_transfer'}),
         name='transfer_money'),
    path('account/freeze', AccountsController.as_view({'get': 'get_freeze'}), name='freeze_acc'),
    path('del', AccountsController.as_view({'get': 'get_bloke'}), name='bloke_acc'),
    path('installments', InstallmentsController.as_view({'get': 'get'}), name='my_installments'),
    path('credits', CreditsController.as_view(), name='my_credits'),
    path('add/installments', InstallmentsController.as_view({'get': 'get_create_installment',
                                                             'post': 'post_create_installment'}),
         name='new_installment'),
]
