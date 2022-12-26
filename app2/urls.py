from django.urls import path
from app2.views import *
app_name='somgthing2'
urlpatterns=[
    path('raja/',raja,name='raja'),
    path('rani/',rani,name='rani'),
]