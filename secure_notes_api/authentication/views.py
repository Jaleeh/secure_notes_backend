
from django.shortcuts import render
from rest_framework import generics,response,serializers,status
from rest_framework.generics import GenericAPIView
from .serializers import RegisterUserSerializer,UserListSerializer,LoginUserSerializer
from .models import UserData
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate

# view for registering users
class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request): #send POST request
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status = status.HTTP_201_CREATED)
        return response.Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)

class LoginAPView(GenericAPIView): #send POST request
    serializer_class = LoginUserSerializer
    authentication_classes = (JWTAuthentication,) #uses simple jwt authentication
    
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        clear = {}
        user = authenticate(username = email,password = password)

        if user: #if user exists
            refresh = RefreshToken.for_user(user)
            clear['email'] = user.email
            clear['name'] = user.name
            clear['refresh'] = str(refresh)
            clear['access'] = str(refresh.access_token)
            return response.Response(clear,status=status.HTTP_200_OK)
        return response.Response({'message':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutAPIView(GenericAPIView):    
    def post(self,request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist
        return response.Response('Logout success')

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = IsAdminUser
    queryset = UserData.objects.all()
