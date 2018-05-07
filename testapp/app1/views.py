from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
from .models import Article
# Create your views here.


def base(request):
    return render(request, 'base.html')


def mainview(request, param1):
    article_list = Article.objects.filter(title=param1)
    article = article_list[0]
    article_body = markdown.markdown(article.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    context = {'param1': param1,
               'content': mark_safe(article_body),
               }
    return render(request, 'mainview.html', context)