from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import loginUser, registerUser
from django.contrib.auth.models import User,Group
from django.core.exceptions import ObjectDoesNotExist
from .models import Homework, Record
from django.http import JsonResponse,HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django .http import StreamingHttpResponse

# Create your views here.

def login_user(request):
    """
    登陆操作部分
    :return: 登陆成功跳转至个人主页，失败则提示失败信息。
    """
    if request.method == 'POST':
        form = loginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='Student').exists():
                    return HttpResponseRedirect('/Acount/')
                else:
                    return  HttpResponseRedirect('/Teacher/')
            else:
                messages.error(request, 'Login Failed!')
    else:
        form = loginUser()
    return render(request,'login.html',{'form':form})

def register_user(request):
    if request.method == 'POST':
        form = registerUser(request.POST)
        if form.is_valid():
            if form.cleaned_data['Password']==form.cleaned_data['ConfirmPass']:
                username = form.cleaned_data['Username']
                if User.objects.filter(username__exact=username).count()==0:
                    password = form.cleaned_data['Password']
                    user = User.objects.create_user(username=username,password=password)
                    user.groups.add(Group.objects.get(name='Student'))
                    user.save()
                    messages.success(request, 'Register Successfully!')
                else:
                    messages.error("User has registered")
            else:
                messages.error(request, 'Passwords do not match!')

    else:
        form = registerUser()
    return render(request,'register.html',{'form':form})

@csrf_exempt
def Teacher(request):
    return  render(request,'Teacher.html')

@csrf_exempt
def get_teacher_homeworks(request):
    homeworks = Homework.objects.all()
    resultdict={}
    dict=[]
    count=homeworks.count()
    for h in homeworks:
        dic={}
        dic['id']=h.pk
        dic['des']=h.Description
        dic['duedate']=h.Deadline
        dict.append(dic)
    resultdict['data'] = dict
    resultdict['code'] = 0
    resultdict['msg'] = ""
    resultdict['count'] = count
    return JsonResponse(resultdict, safe=False)

@csrf_exempt
def Account(request):
    """
    个人主页

    :return: 渲染个人主页
    """
    return render(request,'Account.html')

@csrf_exempt
def get_homeworks(request):
    """
    处理数据库中作业相关信息，将其转化为json文件以供前端渲染

    :return: 返回一个包含所有作业信息的json文件
    """

    homeworks = Homework.objects.all()
    resultdict = {}
    dict = []
    count = homeworks.count()
    for h in homeworks:
        dic={}
        dic['id']=h.pk
        dic['des']=h.Description
        dic['duedate']=h.Deadline
        if Record.objects.filter(Homework=h).filter(Student=request.user).count()>0:
            dic['status']="已提交"
            if Record.objects.filter(Homework=h).get(Student=request.user).status==2:
                dic['grade']=Record.objects.filter(Homework=h).get(Student=request.user).Scores
            else:
                dic['grade']='老师尚未打分'
        else:
            dic['status']="未提交"
        dict.append(dic)
    resultdict['data']=dict
    resultdict['code'] = 0
    resultdict['msg'] = ""
    resultdict['count'] = count
    return JsonResponse(resultdict,safe=False)

@csrf_exempt
def upload_file(request, pk):
    """
    处理上传文件

    :return: 如果上传成功并成功保存，则返回一个json文件，其中statu=1表示成功，status=0则表示失败
    """
    file = request.FILES.get('file')
    filename = '%s/%s'%(settings.MEDIA_ROOT, file.name)
    with open(filename,'wb')as f:
        for ff in file.chunks():
            f.write(ff)

    ret={'status':1}
    uploaded = Homework.objects.get(pk=pk)
    Record.objects.create(Homework=uploaded,Student=request.user,Upload_time=timezone.now(),File=file).save()

    return  JsonResponse(ret)

@csrf_exempt
def assign(request):
    if request.method == 'POST':
        Homework.objects.create(Description=request.POST.get('Description'),Deadline=request.POST.get('Deadline')).save()
        ret={'status':1}
        return render(request,'Teacher.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfully!')
    return  render(request, 'logout.html')

@csrf_exempt
def download_homework(request, pk):
    def file_iterator(file, chunk_size=512):
        with open(file) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    r=Record.objects.filter(pk=pk)
    file = r.File
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    return  response

@csrf_exempt
def Record_List(request,pk):
    records = Record.objects.filter(pk=pk)
    resultdict = {}
    dict = []
    count = records.count()
    for r in records:
        dic = {}
        dic['id']= r.Student.username
        dic['homework']=r.Homework.Description
        dic['status']=r.get_status_display()
        dict.append(dic)

    resultdict['data'] = dict
    resultdict['code'] = 0
    resultdict['msg'] = ""
    resultdict['count'] = count
    return JsonResponse(resultdict, safe=False)

@csrf_exempt
def Specific(request,pk):
    return render(request,'Record.html', {'pk':pk})

@csrf_exempt
def grade(request,pk,id):
    if request.method == 'POST':
        record = Record.objects.filter(Homework_id__exact=pk).get(Student__username__exact=id)
        record.Scores=request.POST.get('grade')
        record.status=2
        record.save()
        return render(request, 'Teacher.html')
