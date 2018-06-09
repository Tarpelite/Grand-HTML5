from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class Homework(models.Model):
    Description = models.CharField(max_length=50,blank=True)
    Deadline = models.DateTimeField()

class Record(models.Model):
    Homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    Student = models.ForeignKey(User, on_delete=models.CASCADE, default="44436")
    Upload_time = models.DateTimeField()
    File = models.FileField()
    ToJudge = 1
    Judged = 2
    Late = 3
    Downloaded = 4
    Status_Choice = (
        (ToJudge, '待评判'),
        (Judged, '已评判'),
        (Late, '迟交'),
        (Downloaded, '已下载'),
    )
    status = models.FloatField(choices=Status_Choice, default=ToJudge)
    Scores = models.FloatField(default=0)