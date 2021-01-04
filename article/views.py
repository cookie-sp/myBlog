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