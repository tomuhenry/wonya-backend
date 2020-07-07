from django.contrib import admin
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
]
