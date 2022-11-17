from django.urls import path,include
from login import views

urlpatterns = [
    path('', views.Login,name='login'),
    
]