from django.urls import path
from .views import HomeView, ContractDetailsView, UserFunctionsView, GetAccountBalanceView, OwnerFunctionsView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('contract-details/', ContractDetailsView.as_view(), name='contract-details'),
    path('user-functions/', UserFunctionsView.as_view(), name='user-functions'),
    path('owner-functions/', OwnerFunctionsView.as_view(), name='owner-functions'),
    path('get-account-balance/', GetAccountBalanceView.as_view(), name='get-account-balance'),
]
