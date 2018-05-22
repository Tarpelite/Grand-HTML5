from django.db import models
STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}

# Create your models here.
class User(models.Model):
    identity_type_choices = {
        ('stu', 'Student'),
        ('Teac', 'Teacher')
    }
    identity = models.CharField(max_length=10, verbose_name=u'身份', choices=identity_type_choices, default='stu')
    stu_id = models.CharField(max_length=30, verbose_name=u'学号/工作号', blank=False, unique=True)
    college_name = models.CharField(max_length=30, blank=True)
    Username = models.CharField(max_length=30, verbose_name=u'昵称')
    passwd = models.CharField(max_length=30, verbose_name=u'密码')
    email = models.EmailField(max_length=30, verbose_name=u'邮箱')

    def __unicode__(self):
        return self.Username

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题',unique=True)
    author = models.ForeignKey('User', verbose_name=u'作者', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name=u'栏目', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    body = models.TextField(u'正文', max_length=1000)
    staus = models.IntegerField(default=0, choices=STATUS.items())

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    p_node = models.ForeignKey('Comment', null= True, blank=True, related_name='my_child_comment', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1024)

    def __str__(self):
        return self.comment




