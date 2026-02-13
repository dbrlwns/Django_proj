from django.urls import path
from users.views import user_auth

urlpatterns = [
    path('', user_auth, name='user_auth'),
]