from django.urls import path
from . import views

#create url and open that page followed by function  and name is just reference 
urlpatterns=[
    path('',views.show,name='show index'),
    path('index/',views.index ,name="index")
]