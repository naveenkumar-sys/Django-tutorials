from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. handle render and  http request 
#here HTTP request is the request that is sent from the browser to the server and automatically visible in ui

def show(request):
    return HttpResponse("<h1>Welcome to my Django tutorial</h1>")


def index(request):
    return HttpResponse("<h1>THis is second page</h2>")

def home(request):
    return render(request,'index.html')