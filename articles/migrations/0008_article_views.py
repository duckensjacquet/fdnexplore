# Generated by Django 4.1.3 on 2022-11-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_status_alter_article_imagecaptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
