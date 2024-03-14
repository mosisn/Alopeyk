from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Account, Order
from django.contrib.auth.hashers import make_password
from .serializers import AccountSerializer, OrderSerrializer
from random import randint



class AccountList(APIView):
    
    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            otp = randint(11111, 99999)
            serializer.validated_data['otp'] = otp
            password = serializer.validated_data.get('password')
            if password:
                user = serializer.save()
                user.set_password(password)
                user.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerrializer