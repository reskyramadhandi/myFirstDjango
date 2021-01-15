from django.shortcuts import render

nav = [
    ['/', 'Home'],
    ['/blog', 'Blog'],
    ['/about', 'About'],
    ['/contact', 'Contact'],
]
# Create your views here.


def index(request):
    context = {
        'app': 'About',
        'judul': 'Resky\'s First Django',
        'creator': 'reskyramadhandi',
        'banner': 'about/img/banner_about.png',
        'nav': nav,
    }
    return render(request, 'about/index.html', context)
