from django.shortcuts import render

# Create your views here.
"""для регистрации"""
from rest_framework import generics , views
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import ProfileSerializer , AllSerializers
"""для логина"""
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import Profile
from rest_framework.permissions import IsAuthenticated



class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()                         
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    
    def post(self, request, format=None):            #если не заполнят что-то упадет система заберет none
        data = request.data
        mail = data.get('mail', None)
        password = data.get('password', None)

        if mail is None or password is None:
            return Response({'Ошибка! Проверьте логин или пароль!'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(mail=mail, password=password)

        if not user:
            return Response({'Ошибка! Такой пользователь не зарегистрирован'}, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
    
class AllProfileView(generics.CreateAPIView):
    
    model = Profile                   
    serializer_class = AllSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        all = Profile.objects.all()             
        return all

        