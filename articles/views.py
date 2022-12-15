from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article,Banner,OrganizationAbout,Slide

def Index(request):
    try:
        #Retrieve the last article with his Id
        allArticle=Article.objects.all()
        lastarticle=Article.objects.all().order_by("-id")[0]
        lastid=lastarticle.id
        #retrieve all articles exclude the last article and order by id desc
        article=Article.objects.all().order_by("-id").exclude(id = lastid)
        #retrieve the banner that is active
        banner=Banner.objects.all().filter(isactive=True)
        #retrieve the org about
        about=OrganizationAbout.objects.all().filter(is_active=True)
        #Paginator the articles
        page_num=request.GET.get('page',1)
        paginator=Paginator(article,6)
        try:
            page_obj=paginator.page(page_num)
        except PageNotAnInteger:
            page_obj=paginator.page(1)
        except EmptyPage:
            page_obj=paginator.page(paginator.num_pages)
        #retrieve the photos slide
        slide=Slide.objects.all()
        #create the context
        context={'articles': article,'lastarticle': lastarticle,'banner': banner,'abouts':about,'slides': slide,'page_obj': page_obj}
        return render(request,'articles/index.html',context)
    except:
        pass
    

def DisplayArticle(request,id):
    article=Article.objects.get(pk=id)
    article.views+=1
    article.save()
    return render(request,'articles/display.html',{'article' : article})


def DeleteArticle(request,id):
    article=Article.objects.get(pk=id)
    article.delete()
    return render(request,'dashboardadmin/articles.html',{'article' : article})
