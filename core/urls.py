from os import name
from django.urls import path
from . import views

app_name = "core"
urlpatterns=[
    path('', views.index, name='index'),
    path('yourstory', views.yourstory, name="yourstory"),
    path('hackernews',views.hackernews,name='hackernews'),
]