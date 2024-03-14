from rest_framework import serializers
from .models import Account, Order
from django.contrib.auth.models import User, Group


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'phone_number', 'role', 'password', 'otp']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class OrderSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'