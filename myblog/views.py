from django.shortcuts import render

# Create your views here.
import markdown
import pygments
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404


def index(request):
    article_list = Article.objects.all().order_by('-created_time')  # -created_time 逆序排序
    return render(request, 'myblog/index.html', context={'article_list': article_list})
    # return render(request, 'myblog/index.html', context={
    #     'title': 'index_page',
    #     'welcome': 'welcome to my blog'
    # })
    # return HttpResponse("welcome to my blog!")


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.article_text = markdown.markdown(article.article_text,
                                             extensions=[
                                                 'markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc',
                                             ])
    return render(request, 'myblog/detail.html', context={'article': article})

