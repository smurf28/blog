from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.urls import reverse


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=70)
    article_text = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True) # 文章摘要

    category = models.ForeignKey(Category)
    label = models.ForeignKey(Label, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Comments(models.Model):
    name = models.CharField(max_length=100)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.name
