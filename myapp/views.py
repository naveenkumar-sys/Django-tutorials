from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. handle render and  http request 
#here HTTP request is the request that is sent from the browser to the server and automatically visible in ui

def show(request):
    return HttpResponse("<h1>Welcome to my Django tutorial</h1>") #send as response and directly retun in ui


def index(request):
    return HttpResponse("<h1>THis is second page</h2>") #send as response and directly retun in ui

# def home(request):
#     name="Rohit"
  
#     return render(request,'index.html',{'name':name}) #it render the html file  


# def home(request):
#     context={
#         'name':"Naveen",
#         'age':20,
#         'subject':'Django'
#     }
#     return render(request,'index.html',context)  # here we pass the python dictionary but we access in index.hmtl directly variable name , django will automatically break data into 'name':Naveen so we can access directly

def home(request):
    context={
        'name':"Naveen",
        'age':20,
        'subject':'Django'
    }
    return render(request,'index.html',{'context':context})  #here we directly send as json if we want to access in index.html like context.name , context.age
