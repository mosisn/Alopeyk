from django.urls import path
from .views import AccountList, OrderList
urlpatterns = [
    path('register/', AccountList.as_view(), name='register'),
    path('order/',OrderList.as_view(), name='order list' )
]