from django.urls import path,include
from dashboardadmin import views

urlpatterns = [
    path('',views.Dashboard),
     path('newarticle',views.Newarticle,name='newarticle'),
     path('article',views.ListArticle,name='article'),
    
]