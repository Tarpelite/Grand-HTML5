from django.shortcuts import render, render_to_response
from django import forms
from .models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class UserForm(forms.Form):
    id = forms.CharField(label='学号/工号', max_length=30)
    identity = forms.CharField(label='身份', max_length=30)
    email = forms.EmailField(label='邮箱', max_length=30)
    username = forms.CharField(label='用户名', max_length=30)
    passwd = forms.CharField(label='密码', widget=forms.PasswordInput())


def register(request):
    Method = request.method
    if Method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['passwd']
            email = uf.cleaned_data['email']
            id = uf.cleaned_data['id']
            identity = uf.cleaned_data['identity']
            User.objects.create(username=username, passwd=passwd, stu_id=id, email=email,
                                identity=identity, )
            User.save()

            return HttpResponse(u"注册成功！")
    else:
        uf = UserForm()
    return render_to_response('register.html', {'userform': uf})

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passwd = uf.cleaned_data['passwd']

            user = User.objects.filter(username_exact=username, passwd_exact=passwd)

            if user:
                return render_to_response('index.html', {'userform':uf})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'userform':uf})

def logout(request):
    pass