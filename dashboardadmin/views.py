from django.shortcuts import render
from articles.models import Article,Category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Dashboard(request):
    return render(request, 'dashboardadmin/index.html')

def ListArticle(request):
    article=Article.objects.all().order_by("-id")
    return render(request, 'dashboardadmin/articles.html', {'articles': article})

def Newarticle(request):
    category=Category.objects.all()
    article=Article()
    if request.method == 'POST':
        article.title=request.POST['title']
        article.text=request.POST['text']
        article.imagethumbnail=request.FILES['imagethumbnail']
        article.publishedby=User.objects.get(pk=request.user.id)
        article.category=Category.objects.get(pk=int(request.POST['category']))
        article.save()
        article=Article.objects.all().order_by("-id")
        return HttpResponseRedirect(reverse('article'))
    return render(request, 'dashboardadmin/newarticle.html',{'categories': category})
