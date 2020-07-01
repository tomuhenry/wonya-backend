from django.urls import path
from .views import profile, login_view

app_name = 'accounts'

urlpatterns = [
    path('profile', profile, name='profile'),
    path('login/', login_view, name='login'),
]