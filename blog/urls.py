from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('recent/', views.recent),
    path('cerita/', views.cerita),
    path('news/', views.news),
]
