from django.urls import path
from . import views

app_name = 'Auth_app'

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
]