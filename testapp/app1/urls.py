from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.mainview, name='index'),
    path('mainview/<str:param1>', views.mainview)
]