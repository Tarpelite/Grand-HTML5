from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def base(request):
    return render(request, 'base.html')