from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, RegisterSerializer


class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # دریافت داده‌های معتبر
            email = serializer.validated_data['email'].lower()
            full_name = serializer.validated_data['full_name']
            password = serializer.validated_data['password1']

            # ایجاد کاربر
            user = User(email=email, full_name=full_name)
            user.set_password(password)
            user.save()

            # بازگرداندن داده‌های کاربر در پاسخ
            return Response({
                'status': 'Done',
                'email': user.email,
                'full_name': user.full_name
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
