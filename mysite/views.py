# from django.http import HttpResponse
from django.shortcuts import render 
from collections import Counter

def index(request):
    return render(request,'home.html')

def count(request):
    counts = (len(request.GET['text'])) #统计提交文本字数
    content = request.GET['text']   #获取提交文本
    frequency = dict(Counter(content))
    frequency = sorted(frequency.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'counts':counts,'content':content,'frequecy':frequency})

def about(request):
    return render(request,'about.html')
