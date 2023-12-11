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

class SignupView(generics.CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[permissions.AllowAny]

