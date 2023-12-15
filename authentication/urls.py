
from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet,SignupView,ProductView

from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet,SignupView

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
   path('signup/', SignupView.as_view(), name='signup'),
   path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('products/',ProductView.as_view(),name='products'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router=DefaultRouter()
router.register(r'users',UserViewSet, basename='user')
urlpatterns+=[
    path('',include(router.urls)),
]