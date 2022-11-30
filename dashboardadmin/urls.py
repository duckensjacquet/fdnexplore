from django.urls import path,include
from dashboardadmin import views

urlpatterns = [
    path('',views.Dashboard),
     path('newarticle',views.Newarticle,name='newarticle'),
     path('article',views.ListArticle,name='article'),
     path('adduser',views.AddUser,name='adduser'),
     path('users',views.ListUsers,name='users')
    
]