from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Meyuyw Class',
        'subtitle': 'Selamat Datang',
        'subheading': 'Ini adalah kelas terbuka',
        'contributor': 'dhilataha',
        'banner': 'img/banner_home.png',
        'nav': [
            ['/' , 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'], 
            ['/contact', 'Contact'],
        ]
    }
    return render(request, 'index.html', context)

def index2(request):

    judul = "<h1> Hay, meyuyw <h1>"
    subjudul = "<h2>Sub judul nih gais<h2>"

    output = judul + subjudul
    return HttpResponse(output)

