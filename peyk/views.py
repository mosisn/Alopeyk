from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Order
from django.contrib.auth.hashers import make_password
from .serializers import AccountSerializer, OrderSerrializer
from .authentication import create_access_token, create_refresh_token
from random import randint
import traceback


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
            
            return Response({"otp": otp}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FirstLoginView(APIView):
    def post(self, request):
        body = request.data
        phone_number = body.get('phone_number')
        otp = body.get('otp')
        
        try:
            user = Account.objects.get(phone_number=phone_number)
            if user.is_authorized == False:
                if user.otp == otp:
                    user.otp = 0
                    user.is_authorized = True
                    user.save()
                    
                    current_user = Account.objects.get(phone_number=phone_number)
                    access_token = create_access_token(current_user.id)
                    refresh_token = create_refresh_token(current_user.id)
                    
                    res = Response(access_token)
                    res.set_cookie('refresh_token', refresh_token, httponly=True)
                    
                    return res
                else:
                    return Response("Otp is Wrong!", status=status.HTTP_403_FORBIDDEN)
            else:
                return Response("User is already authorized")
        except Account.DoesNotExist:
            return Response("User not found with the provided phone number", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            traceback.print_exc()
            return Response("An error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        body = request.data
        phone_number = body.get('phone_number')
        password = body.get('password')
        hashed_password = make_password(password)
        try:
            user = Account.objects.get(phone_number=phone_number)
            if user.password == hashed_password:
                current_user = Account.objects.get(username=phone_number)
                access_token = create_access_token(current_user.id)
                refresh_token = create_refresh_token(current_user.id)
                res = Response(access_token)
                res.set_cookie('refresh_token', refresh_token, httponly=True)
                return res
            else:
                return Response("password is Wrong!", status=403)
        except:
            return Response("Something is Wrong!", status=500)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerrializer