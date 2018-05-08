from django.db import models
from django.conf import settings
# Create your models here.
STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}


class Nav(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'导航条内容')
    url = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(default=0, choices=STATUS.items())


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True,
                               verbose_name=u'上级分类', on_delete=models.CASCADE)
    href = models.CharField(max_length=200, verbose_name=u'链接', blank=True, null=True)
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'分类'
        ordering = ['rank', '-create_time']

    def __unicode__(self):
        if self.parent:
            return '%s>>%s' % (self.parent, self.name)
        else:
            return '%s' % (self.name)

    def get_parent(self):
        if self.parent:
            return True
        else:
            return False

    __str__ = __unicode__


class Article(models.Model):
    text_type_choices = {
        ('h5', 'HTML5'),
        ('md', 'markdown'),
    }
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=u'分类', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=u'标题')
    en_title = models.CharField(max_length=100, verbose_name=u'英文标题')
    img = models.CharField(max_length=200,
                           default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=200, null=True, blank=True,
                            verbose_name=u'标签', help_text=u'用逗号分隔')
    content = models.TextField(verbose_name=u'正文')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name='状态')
    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    url = models.CharField(max_length=200, verbose_name=u'链接', blank=True)
    text_type = models.CharField(max_length=10, verbose_name=u'正文文本类型', choices=text_type_choices, default='md')

    def get_tags(self):
        tags_list = self.tags.split(',')
        while '' in tags_list:
            tags_list.remove('')
        return tags_list

    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['rank', '-pub_time', '-create_time']

    def __unicode__(self):
        return self.title

    __str__ = __unicode__
