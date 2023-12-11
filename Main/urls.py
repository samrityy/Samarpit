
from django.contrib import admin
from django.urls import path, include

from authentication.views import UserViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')), 
    path('user/',include('authentication.urls')),
    # path('accounts/', include('allauth.urls')),

    # path('rest-auth/', include('rest_auth.urls')),
   
    


]
