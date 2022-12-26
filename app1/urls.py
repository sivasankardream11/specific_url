from django.urls import path
from app1.views import *
app_name='somgthing1'
urlpatterns=[
    path('first/',first,name='first'),
    path('secound/',secound,name='secound'),

]