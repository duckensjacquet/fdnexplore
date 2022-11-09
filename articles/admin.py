from django.contrib import admin
from articles.models import Article, Category, OrganizationAbout, Banner, Slide

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(OrganizationAbout)
admin.site.register(Banner)
admin.site.register(Slide)
