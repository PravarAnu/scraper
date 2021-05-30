from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import datetime
def yourstory(request):
    l = []
    url = 'https://yourstory.com/feed'
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")
    for n, t in enumerate(soup.findAll("title")):
        # print(str(n) + " - "+ t.text)
        l.append(str(n) + " - " + t.text)
    l.pop(0)
    todays_date = datetime.datetime.now()
    return render(request,'core/home.html',{'links':l,'date':todays_date})


def index(request):
    return render(request, 'core/landing.html')

