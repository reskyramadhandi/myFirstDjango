from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'app': 'Home',
        'judul': 'Resky\'s First Django',
        'creator': 'reskyramadhandi',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ],
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def oldindex(request):
    return HttpResponse("<h1> Halo Dunia </h1>")


def oldabout(request):
    return HttpResponse("Ini About")
