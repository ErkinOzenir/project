from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from django.shortcuts import get_object_or_404

class LogoutAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"success": "User logged out"})
  # def get_serializer_class(self):
  #   user = self.request.user
  #   if user.is_superuser:
  #       return SerializerClassWithHigherPermissions
  #   elif user.is_staff:
  #       return SerializerClassWithIntermediatePermissions
  #   else:
  #       return SerializerClassWithCustomerPermissions

class LoginAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny),
  serializer_class = LoginAPISerializer
  def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      
      user = authenticate(username=username, password=password)
      if user is not None:
          login(request, user)
          token, created = Token.objects.get_or_create(user=user)
          return Response({'token': token.key})
      else:
          return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user =  get_object_or_404(User, id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['tags', 'author']