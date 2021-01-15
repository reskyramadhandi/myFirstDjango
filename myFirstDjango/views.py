from django.http import HttpResponse
from django.shortcuts import render

nav = [
    ['/', 'Home'],
    ['/blog', 'Blog'],
    ['/about', 'About'],
    ['/contact', 'Contact'],
]


def index(request):
    context = {
        'app': 'About',
        'judul': 'Resky\'s First Django',
        'creator': 'reskyramadhandi',
        'banner': 'img/banner_home.png',
        'nav': nav,
    }
    return render(request, 'index.html', context)


def oldindex(request):
    return HttpResponse("<h1> Halo Dunia </h1>")


def oldabout(request):
    return HttpResponse("Ini About")
