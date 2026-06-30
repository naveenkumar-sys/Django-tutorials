from django.urls import path
from . import views

#create url and open that page followed by function  and name is just reference 
urlpatterns=[
    path('first/',views.show,name='show index'),  #http://127.0.0.1:8000/first ,  inside views module function is called , name is just reference
    path('second/',views.index ,name="index"),
    path('',views.home,name='home page')
]