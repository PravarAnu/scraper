from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

from django.utils import timezone

from .forms import Feedback
from .models import UserFeedback
from django.http import HttpResponse

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

def about(request):

    if request.method=="POST":
        feedback_obj=Feedback(request.POST)
        if feedback_obj.is_valid():
            email_val=feedback_obj.cleaned_data['email']
            feedback_val=feedback_obj.cleaned_data['feedback']
            UserFeedback_obj=UserFeedback(email=email_val,feedback=feedback_val,date=timezone.now())
            UserFeedback_obj.save()
            feedback_obj=Feedback()
            
    else:
        feedback_obj=Feedback()
    latest_feedback_list = UserFeedback.objects.order_by("-date")[:5]
    return render(request,'core/about.html',{
        'form':feedback_obj,
        'latest_feedback':latest_feedback_list
    })

