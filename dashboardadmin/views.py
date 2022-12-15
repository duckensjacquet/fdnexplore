from django.shortcuts import render
from articles.models import Article,Category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Dashboard(request):
    nbarticle=Article.objects.all().count()
    nbuser=User.objects.all().count()
    article=Article.objects.all().order_by("-views")[:5]
    return render(request, 'dashboardadmin/index.html',{'nbarticle': nbarticle,'nbuser': nbuser,'marticles': article})

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


def DeleteArticle(request,id):
    articleToDelete=Article.objects.get(pk=id)
    article=Article.objects.all().order_by("-id")
    #if articleToDelete is not None:
        #articleToDelete.delete()
        #return HttpResponseRedirect(reverse('article'))
    return render(request,'dashboardadmin/deletearticle.html',{ 'delarticle': articleToDelete,'articles': article})


def ConfirmDeleteArticle(request,id):
    delart=Article.objects.get(pk=id)
    if delart is not None:
        delart.delete()
        return HttpResponseRedirect(reverse('article'))
    article=Article.objects.all().order_by("-id")
    return render(request, 'dashboardadmin/articles.html', {'articles': article})


def UpdateUser(request,id):
    user=User.objects.get(pk=id)
    if request.method == 'POST':
        user.first_name=request.POST['firstname']
        user.last_name=request.POST['lastname']
        user.username=request.POST['username']
        user.email=request.POST['email']
        if request.POST['password'] is not None or request.POST['password'] !='':
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
    return render(request, 'dashboardadmin/adduser.html',{'user':user})

def UpdateArticle(request,id):
    article=Article.objects.get(pk=id)
    if request.method == 'POST':
        article.title=request.POST['title']
        article.text=request.POST['text']
        if request.FILES['imagethumbnail'] is not None:
            article.imagethumbnail=request.FILES['imagethumbnail']
        article.publishedby=User.objects.get(pk=request.user.id)
        article.category=Category.objects.get(pk=int(request.POST['category']))
        if request.FILES['caption'] is not None:
            article.imagecaptions=request.POST['caption']
        article.save()
    return render(request,'dashboardadmin/newarticle.html',{'article':article})