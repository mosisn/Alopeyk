from django.urls import path
from .views import AccountList, OrderList, FirstLoginView, LoginView


urlpatterns = [
    path('register/', AccountList.as_view(), name='register'),
    path('register/auth', FirstLoginView.as_view(), name='first time login'),
    path('login/',LoginView.as_view(), name='login with password'),
    path('order/',OrderList.as_view(), name='order list' )
]