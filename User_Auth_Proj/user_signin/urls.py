from django.urls import path, re_path, include
from user_signin import views

app_name = 'user_signin'

urlpatterns = [
    path('register/', views.register,  name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
