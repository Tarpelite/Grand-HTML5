"""FileUpload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from upload import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('register/',views.register_user, name='register'),
    path('Acount/',views.Account),
    path('get_homeworks/',views.get_homeworks,name='get_homeworks'),
    path('Acount/upload_file/<int:pk>/',views.upload_file,name='upload_file'),
    path('Teacher/',views.Teacher),
    path('get_teacher_homeworks',views.get_teacher_homeworks,name='get_teacher_homeworks'),
    path('Teacher/assign/',views.assign,name='assign'),
    path('Logout',views.logout, name='logout'),
    path('Teacher/download_all/<int:pk>', views.download_homework),
    path('Teacher/<int:pk>', views.Specific, name='des'),
    path('Teacher/<int:pk>/get', views.Record_List, name='get_records'),
    path('Teacher/<int:pk>/grade/<int:id>/', views.grade)
]
