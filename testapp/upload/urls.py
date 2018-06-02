from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/',views.register_user, name='register'),
    path('Account/',views.Account),
    path('get_homeworks/',views.get_homeworks, name='get_homeworks'),
    path('upload_file/',views.upload_file,name='upload_file'),
]