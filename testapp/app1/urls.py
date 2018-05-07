from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.base, name='index'),
    re_path(r'^mainview/(.+)$', views.mainview)
]