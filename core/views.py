from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

def yourstory(request):
    l = []
    url = 'https://yourstory.com/feed'
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")
    for n, t in enumerate(soup.findAll("title")):
        l.append(str(n) + " - " + t.text)
    l.pop(0)
    todays_date = datetime.datetime.now()
    return render(request,'core/yourstory.html',{'links':l,'date':todays_date})

def hackernews(request):
    url='https://news.ycombinator.com/'
    l=[]
    content = urlopen(url).read()
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        l.append(str(i+1)+' - '+tag.text + '\n') if tag.text!='More' else ''
    todays_date = datetime.datetime.now()
    return render(request,'core/hackernews.html',{'links':l,'date':todays_date})
       

def index(request):
    return render(request, 'core/landing.html')

