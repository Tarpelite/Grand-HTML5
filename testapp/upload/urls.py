from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('Account/', views.Account),
    path('get_homeworks/', views.get_homeworks, name='get_homeworks'),
    path('Account/upload_file/<int:pk>/', views.upload_file, name='upload_file'),
    path('Teacher/', views.Teacher),
    path('get_teacher_homeworks', views.get_teacher_homeworks, name='get_teacher_homeworks'),
    path('assign/', views.assign, name='assign'),
    path('logout/', views.logout_view, name='logout'),
    path('Teacher/<int:pk>', views.Specific, name='des'),
    path('Teacher/<int:pk>/get', views.Record_List, name='get_records'),
    path('Teacher/<int:pk>/download/<int:id>', views.download_homework),
    path('Teacher/<int:pk>/grade/<int:id>/', views.grade)
]