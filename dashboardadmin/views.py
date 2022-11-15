from django.shortcuts import render
from articles.models import Article,Category

# Create your views here.

def Dashboard(request):
    return render(request, 'dashboardadmin/index.html')



def Newarticle(request):
    category=Category.objects.all()
    article=Article()
    if request.method == 'POST':
        article.title=request.POST['title']
        article.text=request.POST['text']
        article.category=Category.objects.get(pk=int(request.POST['category']))
        article.save()
        return render(request, 'dashboardadmin/newarticle.html')
    return render(request, 'dashboardadmin/newarticle.html',{'categories': category})
