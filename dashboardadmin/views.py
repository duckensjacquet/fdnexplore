from django.shortcuts import render
from articles.models import Article,Category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Dashboard(request):
    nbarticle=Article.objects.all().count()
    nbuser=User.objects.all().count()
    return render(request, 'dashboardadmin/index.html',{'nbarticle': nbarticle,'nbuser': nbuser})

def ListArticle(request):
    article=Article.objects.all().order_by("-id")
    return render(request, 'dashboardadmin/articles.html', {'articles': article})

def ListUsers(request):
    users=User.objects.all()
    return render(request, 'dashboardadmin/listuser.html', {'users': users})

def Newarticle(request):
    category=Category.objects.all()
    article=Article()
    if request.method == 'POST':
        article.title=request.POST['title']
        article.text=request.POST['text']
        article.imagethumbnail=request.FILES['imagethumbnail']
        article.publishedby=User.objects.get(pk=request.user.id)
        article.category=Category.objects.get(pk=int(request.POST['category']))
        article.imagecaptions=request.POST['caption']
        article.save()
        article=Article.objects.all().order_by("-id")
        return HttpResponseRedirect(reverse('article'))
    return render(request, 'dashboardadmin/newarticle.html',{'categories': category})


def AddUser(request):
    if request.method == 'POST':
        if len(request.POST['username']) < 0 or len(request.POST['password'])<6:
            print('sorry')
        else:
            user=User()
            user.first_name=request.POST['firstname']
            user.last_name=request.POST['lastname']
            user.username=request.POST['username']
            user.email=request.POST['email']
            user.password=request.POST['password']
            if request.POST.get('staff','')=='on':
                user.is_staff=True
            else:
                user.is_staff=False
            if request.POST.get('superuser','')=='on':
                user.is_superuser=True
                user.is_staff=True
            else:
                user.is_superuser=False
            user.save()
    return render(request, 'dashboardadmin/adduser.html')