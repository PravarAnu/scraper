from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import datetime

l=[]
url='https://yourstory.com/feed'
content = requests.get(url).content
soup = BeautifulSoup(content, "html.parser")
for n,t in enumerate(soup.findAll("title")):
    # print(str(n) + " - "+ t.text)
    l.append(str(n) + " - "+ t.text)

l.pop(0)

def home(request):
    todays_date=datetime.datetime.now()
    return render(request,'core/home.html',{'links':l,'date':todays_date})


