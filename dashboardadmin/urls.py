from django.urls import path,include
from dashboardadmin import views

urlpatterns = [
    path('',views.Dashboard),
     path('newarticle',views.Newarticle,name='newarticle'),
     path('article',views.ListArticle,name='article'),
     path('adduser',views.AddUser,name='adduser'),
     path('users',views.ListUsers,name='users'),
     path('article/<int:id>',views.DeleteArticle,name='deletearticle'),
     path('article/delete/<int:id>',views.ConfirmDeleteArticle,name='confirmdeletearticle'),
     path('updateuser/<int:id>',views.UpdateUser,name='updateuser'),
     path('updatearticle/<int:id>',views.UpdateArticle,name='updatearticle')
    
]