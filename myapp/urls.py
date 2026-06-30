from django.urls import path
from . import views

#create url and open that page followed by function  and name is just reference 
urlpatterns=[
    path('first/',views.show,name='show index'),
    path('second/',views.index ,name="index"),
    path('',views.home,name='home page')
]