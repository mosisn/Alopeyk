from rest_framework import serializers
from .models import Account, Order
from django.contrib.auth.models import User, Group


class AccountSerializer(serializers.ModelSerializer):
    model = Account
    fields = '__all__'

class UserSrializers(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'password', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    model = Group
    fields = ['id', 'name']

class OrderSerrializer(serializers.ModelSerializer):
    model = Order
    fields = '__all__'