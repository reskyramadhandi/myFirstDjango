from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'app': 'Blog',
        'page': 'Home',
        'judul': 'Resky\'s First Django',
        'contributor': 'Mario Ucup',
        'creator': 'reskyramadhandi',
    }
    return render(request, "blog/index.html", context)


def recent(request):
    context = {
        'app': 'Blog',
        'page': 'Recent',
        'judul': 'Resky\'s First Django',
        'contributor': 'Mario Ucup',
        'creator': 'reskyramadhandi',
    }
    return render(request, "blog/index.html", context)


def news(request):
    context = {
        'app': 'Blog',
        'page': 'News',
        'judul': 'Resky\'s First Django',
        'contributor': 'Asep Oblong',
        'creator': 'reskyramadhandi',
    }
    return render(request, "blog/index.html", context)


def cerita(request):
    context = {
        'app': 'Blog',
        'page': 'Cerita',
        'judul': 'Resky\'s First Django',
        'contributor': 'Sandra Bulog',
        'creator': 'reskyramadhandi',
    }
    return render(request, "blog/index.html", context)
