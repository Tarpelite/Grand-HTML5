from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponseNotFound, Http404
import markdown
from .models import Article, Category
# Create your views here.


class Bar:
    name = ""
    subBar = []
    def __init__(self, name):
        self.name = name


def base(request):
    return render(request, 'base.html')

def get_catogary():
    catogary_list = Category.objects.all().order_by('rank')
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
        if len(article_tmp) > 0:
            for i in article_tmp:
                directory_dict[dir.name].append(i.name)


def mainview(request, param1='课程介绍'):
    article_list = Article.objects.filter(title=param1)
    if len(article_list) == 0:
        return HttpResponseNotFound("<h1>Page not found</h1></br><a href='课程概况'>点击这里返回主页")
    article = article_list[0]
    article_path = "当前位置:"+str(article.category)+">>"+article.title

    context = {'param1': param1,
               'path': article_path,
               }
    if article.text_type == 'md':
        '''正文文本是markdown语法'''
        article_body = mark_safe(markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ]))
    else:
        '''正文文本是h5语法'''
        context['h5'] = 'Yes'
        article_body = article.content


    context['content'] = article_body
    catogary_list = Category.objects.all()
    directory = []
    Bars = []
    for q in catogary_list:
        if not q.parent:
            directory.append(q)
    #directory_name = []

    cnt = 0
    for dir in directory:
        tmp = []
        tmp.append(dir.name)
        #directory_name.append(dir.name)
        #context[dir.name] = []

        article_tmp = Article.objects.filter(category=dir)
        if len(article_tmp) > 0:
            for i in article_tmp:
                #Bars[cnt].subBar.append(i.title)
                tmp.append(i.title)
        Bars.append(tmp)


    #print(directory_name)
    #print(Bars)
    #context['directory_name'] = directory_name
    context['Bars'] = Bars
    return render(request, 'mainview.html', context)