from django.urls import path
from users.views import user_login, user_logout, user_register, user_update

urlpatterns = [
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', user_register, name='user_register'),
    path('register/', user_register, name='user_register'),
    path('update/', user_update, name='user_update'),

]