
from django.shortcuts import render
from requests import Response, request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Products
from .serializer import UserSerializer, SignupSerializer,ProductsSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, SignupSerializer
from rest_framework import generics, permissions



class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,]
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()

    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 2
        page_size_query_param = 'page_size'
        max_page_size = 10
    pagination_class = StandardResultsSetPagination


class SignupView(generics.CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[permissions.AllowAny]


class ProductView(generics.CreateAPIView):
    serializer_class=ProductsSerializer
    queryset=Products.objects.all()
