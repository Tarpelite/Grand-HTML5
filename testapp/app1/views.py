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
    directory = []
    directory_dict = {}

    for q in catogary_list:
        if not q.parent:
            directory.append(q)
    directory_name = []

    for dir in directory:
        directory_name.append(dir.name)
        directory_dict[dir.name] = []
        article_tmp = Article.objects.filter(parent=dir)
        if len(article_tmp)>0:
            for i in article_tmp:
                directory_dict[dir.name].append(i.name)

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
    catogary_list = Category.objects.all()
    directory = []
    #directory_dict = {}

    for q in catogary_list:
        if not q.parent:
            directory.append(q)
    directory_name = []

    for dir in directory:
        directory_name.append(dir.name)
        context[dir.name] = []

        article_tmp = Article.objects.filter(category=dir)
        if len(article_tmp) > 0:
            for i in article_tmp:
                context[dir.name].append(i.title)

    print(directory_name)
    context['directory_name'] = directory_name
    return render(request, 'mainview.html', context)