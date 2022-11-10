from django.shortcuts import render
from articles.models import Article,Banner,OrganizationAbout,Slide

def Index(request):
    #Retrieve the last article with his Id
    lastarticle=Article.objects.all().order_by("-id")[0]
    lastid=lastarticle.id
    #retrieve all articles exclude the last article and order by id desc
    article=Article.objects.all().order_by("-id").exclude(id = lastid)
    #retrieve the banner that is active
    banner=Banner.objects.all().filter(isactive=True)
    #retrieve the org about
    about=OrganizationAbout.objects.all().filter(is_active=True)
    #retrieve the photos slide
    slide=Slide.objects.all()
    #create the context
    context={'articles': article,'lastarticle': lastarticle,'banner': banner,'abouts':about,'slides': slide}
    return render(request,'articles/index.html',context)


#--web: gunicorn fdnexplore.wsgi --log-file -
    

