### 1.软件的安装

1. VSCode下载（安装python，chinese，path intellisence，npm，npm intellisence，Vetur，VUE3 Snipper，vscode-icons，live-server）

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX

4. 安装小程序开发项目

### 二.git仓库

1. 安装git
2. 创建远程仓库myBlog
3. 初始化本地仓库,也就是再本地的myBlog文件夹下执行:`git init`,执行后会创建一个.git隐藏文件
4. 远程仓库和本地仓库进行关联:`git remote add origin '你的远程仓库地址'`
5. 如果出现错误,ssh没有创建
6. 先去创建密钥:ssh keygen,一路enter,生成密钥
7. 查看生成的密钥 cat~/.ssh/id_rsa.pub,将生成的密钥写入github上的settings下的SSH and GPG keys下
8. 推送四步骤
   - git status
   - git add .
   - git commit -m '备注'
   - git push -u origin master 首次提交到远程仓库
   - git push  之后的提交

### 三.创建myBlog项目

1. 空文件夹下,执行`django-admin startproject myBlog `
2. 给myBlog创建虚拟环境,使用:`python -m venv env `
3. 进入虚拟环境,windows:`.\\env\\Scripts\\activate`
4. 退出虚拟环境,windows下:`deactivate`
5. 使用VScode打开myBlog,执行:`python manage.py startapp article `

### 四.创建models

1. 创建models
2. 数据库同步
3. 在admin.py中注册model

### 五. 业务逻辑

1. 文章列表页，分页
2. 文章详情页，评论
3. 全局搜索功能
4. 最新文章，最新评论的排行
5. 按照分类，标签的一个聚类操作
6. 联系我页面，发送邮件

````python
# 1. 创建static和templates文件夹，将静态页面和样式 写入，并在settings对文件夹的目录进行配置
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
# 2.views是models和templates之间的联系
# views.py 
from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request,'index.html',context)


def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article":article
    }
    return render(request,'single_article.html',context)


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
# 3.对路由进行注册，首先在主路由下进行注册，然后在各自的模块中创建urls.py文件，进行细化注册
# 主urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',include("article.urls"))
]
# article/urls.py
from django.urls import path
from article import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<int:pk>',views.detail,name="detail"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about")
]
# 4.对模板文件中样式文件的引入 采用{% load static %}将static文件引入，再通过{% %}引入样式文件
# 5.因为模板文件中有很多重复代码，比如说 header，footer，aside，创建专门的前端代码文件存放这些固定样式，再在不同的页面中，通过代码引入，如下
{% extends 'common/base.html' %}
	
{% block content %}
		不同的内容
{% include 'common/aside.html' %}
{% endblock %}
# 6，模块代码中，有很多内容已经写死了，但是我们想要它随着数据的变化，渲染到页面中
{% for article in articles %}
{{ article.title }}
{{ article.created_at }}
{{ article.abstract }}
{{ article.content | truncatechars:200 }}  # truncatechars:限制可以显示的字数，也可以直接在models定义模型时定义
{% endfor %}
````

