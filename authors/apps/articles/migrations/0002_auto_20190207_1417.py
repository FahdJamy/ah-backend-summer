# Generated by Django 2.1.5 on 2019-02-07 14:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disliked_by',
            field=models.ManyToManyField(
                related_name='disliked_articles',
                related_query_name='disliked_article',
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='liked_by',
            field=models.ManyToManyField(
                related_name='liked_articles',
                related_query_name='liked_article',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
