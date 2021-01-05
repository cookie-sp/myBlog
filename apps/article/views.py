from django.shortcuts import render
from .models import Article,Category,Tag
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    articles = Article.objects.all()
    limited = 2
    p = Paginator(articles,limited)
    # 得到前端传过来的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1

    articles = p.get_page(page)
    # 获取到最新的5篇文章
    lastest_articles = articles[:5]
    # 获取所有的分类
    categories = Category.objects.all()
    # 获取所有的标签
    tags = Tag.objects.all()
    context = {
        "articles":articles,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags
    }
    return render(request,'index.html',context)


def detail(request,pk):
    article = Article.objects.get(pk=pk)
    article.increase_visited()
    print(article.get_absolute_url())
    # 获取到最新的5篇文章
    lastest_articles = Article.objects.all()[:5]
    # 获取所有的分类
    categories = Category.objects.all()
    # 获取所有的标签
    tags = Tag.objects.all()
    context = {
        "article":article,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags
    }
    return render(request,'single_article.html',context)


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def search(request):
    keyword = request.GET.get("keyword")
    print(keyword)
    if not keyword:
        error_msg = "请输入关键字"
        return render(request,'index.html',locals())
    articles = Article.objects.filter(Q(title__icontains = keyword)|Q(abstract__icontains = keyword)|Q(content__icontains=keyword))
    limited = 2
    p = Paginator(articles,limited)
    # 得到前端传过来的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1

    articles = p.get_page(page)
    # 获取最新的5篇文章
    lastest_articles = articles()[:5]
    # 获取所有的分类
    categories = Category.objects.all()
    # 获取所有的标签
    tags = Tag.objects.all()
    # context = {
    #     "articles":articles,
    #     "lastest_articles":lastest_articles,
    #     "categories":categories,
    #     "tags":tags
    # }
    return render(request,'index.html',locals())