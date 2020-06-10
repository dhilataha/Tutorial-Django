from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Open Class',
        'subtitle': 'Tentang Kelas Terbuka',
        'contributor': 'Mey',
        'banner': 'about/img/banner_about.png',
        'app_css': 'about/css/style.css',
    }
    return render(request, 'index.html', context)
