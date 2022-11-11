from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    description = models.CharField(max_length=255,null=True, blank=True)
    createdby= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Article(models.Model):
    category= models.ForeignKey(Category,related_name="category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    text = models.TextField(blank=True, null=True)
    datepublished= models.DateTimeField(auto_now_add=True)
    lastupdated= models.DateTimeField(auto_now=True)
    publishedby= models.ForeignKey(User,  on_delete=models.CASCADE)
    imagethumbnail= models.ImageField(upload_to="articles/static/articles/images/post")
    imagecaptions= models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    bannerimage= models.ImageField(upload_to="articles/static/articles/images/banner")
    bannercaptions= models.CharField(max_length=255, blank=True, null=True)
    dateadded= models.DateField(auto_now=True)
    addedby=models.ForeignKey(User, on_delete=models.CASCADE)
    isactive=models.BooleanField(default="True")

    def __str__(self):
        return self.bannercaptions

class OrganizationAbout(models.Model):
    about= models.TextField(blank=True, null=True)
    is_active= models.BooleanField(default=True, null=True)
    addedby=models.ForeignKey(User, on_delete=models.CASCADE)
    dateadded= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about


class Slide(models.Model):
    photo= models.ImageField(upload_to='articles/static/articles/images/about')
    caption= models.CharField(max_length=225, blank=True, null=True)
    addedby=models.ForeignKey(User, on_delete=models.CASCADE)
    dateadded= models.DateTimeField(auto_now=True)