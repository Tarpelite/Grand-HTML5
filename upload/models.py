from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
    Description = models.CharField(max_length=50,blank=True)
    Deadline = models.DateTimeField()

class Record(models.Model):
    Homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    Student = models.ForeignKey(User, on_delete=models.CASCADE,default="44436")
    Upload_time = models.DateTimeField()
    File = models.FileField()