from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog.html")


def recent(request):
    return render(request, "recent.html")
