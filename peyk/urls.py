from django.urls import path
from .views import AccountList, OrderList, FirstLoginView


urlpatterns = [
    path('register/', AccountList.as_view(), name='register'),
    path('register/auth', FirstLoginView.as_view(), name='first time login'),
    path('order/',OrderList.as_view(), name='order list' )
]