from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Homework
from .models import Record

admin.site.register(Homework)
admin.site.register(Record)
