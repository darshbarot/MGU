from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# admin:-maruti,pass:- maruti4230
# Create your views here.
def home(request):
    return render(request,'index.html')

def contactus(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    obj=contectus()
    obj.name=name
    obj.email=email
    obj.subject=subject
    obj.message=message
    obj.save()
    return render(request,'index.html')