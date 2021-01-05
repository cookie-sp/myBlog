from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128,verbose_name="文章分类",help_text="文章分类")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128,verbose_name="文章标签",help_text="文章标签")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=128,verbose_name="文章内容")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文章作者")
    img = models.ImageField(upload_to="",blank=True,null=True,verbose_name="文章配图")
    abstract = models.TextField(verbose_name="文章摘要")
    content = models.TextField(verbose_name="文章内容")
    category = models.ManyToManyField(Category,verbose_name="文章分类")
    tag = models.ManyToManyField(Tag,verbose_name="文章标签")
    visited = models.IntegerField(default=0,verbose_name="文章访问量")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    modified_at = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        # 排序 如果要按倒序排，在前面加-号
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title

    # 增加访问量
    def increase_visited(self):
        self.visited += 1
        self.save(update_fields = ['visited'])

    # 反向解析，得到每篇文章的绝对路径 http://127.0.0.1:8000/article/detail/2
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.pk)])