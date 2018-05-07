from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
from .models import Article,Category
# Create your views here.


def base(request):
    return render(request, 'base.html')

def get_catogary():
    catogary_list = Category.objects.all()
    bars = []
    bar_names = []
    bar_dict = {}
    for result in catogary_list:
        if not result.get_parent():
            bars.append(result)
            bar_dict[result.name] = []

    for bar in bars:
        sub_bars = Category.objects.filter(parent=bar)
        for i in sub_bars:
            bar_dict[bar.name].append(i.name)


def mainview(request, param1):
    article_list = Article.objects.filter(title=param1)
    article = article_list[0]
    article_path = article.category
    article_body = markdown.markdown(article.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    context = {'param1': param1,
               'content': mark_safe(article_body),
               'path': article_path,
               }
    return render(request, 'mainview.html', context)