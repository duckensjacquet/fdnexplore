"""fdnexplore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from articles import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from dashboardadmin import views as dashboardadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name='index'),
    path('dashboard/',dashboardadmin.Dashboard,name='dash'),
    path('dashboard/',include('dashboardadmin.urls'), name='dashboard'),
    path('login/',include('login.urls'), name='login'),
    path('article/<int:id>', views.DisplayArticle,name='display_article'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
