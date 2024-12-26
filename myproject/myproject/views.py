#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("hello world ")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("This is about section")
    return render(request,'about.html')