from django.contrib.auth.views import (LoginView, LogoutView)
from .views import user_registration
from django.urls import path

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", user_registration, name="register")
]
