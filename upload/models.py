from django.db import models
from django.forms import ModelForm

# Create your models here.
class Homework(models.Model):
    Description = models.CharField(max_length=50,blank=True)
    Deadline = models.DateTimeField()
    Status = models.BooleanField()
    Number = models.IntegerField(default=0)
