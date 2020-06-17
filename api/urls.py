from django.urls import include, path

urlpatterns = [
    path('users/', include('userAuth.urls', namespace='userAuth'))
]
