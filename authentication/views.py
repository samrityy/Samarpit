from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Products
from .serializer import UserSerializer,ProductsSerializer,EmailVerificationSerializer
from rest_framework import generics, permissions,views
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializer import UserSerializer, RegisterSerializer
from rest_framework import generics, permissions,status
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,]
    serializer_class=UserSerializer
    queryset=CustomUser.objects.filter(is_superuser=False, is_staff=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['firstname', 'lastname']
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 10
    pagination_class = StandardResultsSetPagination


# class SignupView(generics.CreateAPIView):
#     serializer_class=SignupSerializer
#     permission_classes=[permissions.AllowAny]
class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]
    
    def post(self,request,*args, **kwargs):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data

        user=CustomUser.objects.get(email=user_data['email'])
        token=RefreshToken.for_user(user).access_token
        
        current_site=get_current_site(request)
        relativeLink=reverse('email-verify')
        
        absurl='http://'+ current_site.domain+relativeLink+"?token="+str(token)
        email_body='Hi '+ user.username+'Use Link to verify email \n'+ absurl
        data={'email_body':email_body,'to_email':user.email,'email_subject':'Verify your email'}
        Util.send_email(data)
        
        return Response(user_data,status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class=EmailVerificationSerializer
    queryset = CustomUser.objects.all()
    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY, description='Description',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token = request.GET.get('token')
        try:   
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user=CustomUser.objects.get(id=payload['user_id'])    
            if not user.is_verified:
                user.is_verified=True
                user.save()
            return Response({'email':'Successfully activated'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'Error':'Error'},status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            print("DecodeError:", identifier)
            return Response({'error':'Invalid'},status=status.HTTP_400_BAD_REQUEST)

class ProductView(generics.CreateAPIView):
    serializer_class=ProductsSerializer
    queryset=Products.objects.all()
