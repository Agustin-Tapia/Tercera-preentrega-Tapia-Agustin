from django.contrib import admin
from django.urls import path, include
from account.views import login_account, register_account 
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login_account, name= "Login"),
    path('logout/', LogoutView.as_view(template_name = "account/logout.html"), name= "Logout"),
    path('register/', register_account, name= "Register"),
]
