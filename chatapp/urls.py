from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    # path("",views.home, name ='home'),
    
    path("",views.login, name ='login'), 
    #set login as home route
    
    path("register",views.register, name ='register'),
]
