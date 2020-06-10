#blogViews

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Open Class',
        'subtitle': 'Blog Kelas Terbuka',
        'contributor': 'dhila',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/style.css',
        'nav': [
            ['/', 'Home'],
            ['/blog/legend', 'Legend'],
            ['/blog/news', 'News'],
        ]
    }
    return render(request, 'index.html', context)

def recent(request):
    return HttpResponse('<h1>ini adalah recent, gais</h1>')


def legend(request):
    context = {
        'title': 'legend',
        'subtitle': 'Blog',
        'contributor': 'Lolly',
    }
    return render(request, 'blog/index.html', context)


def news(request):
    context = {
        'title': 'news',
        'subtitle': 'Blog',
        'contributor': 'Poppy',
    }
    return render(request, 'blog/index.html', context)
