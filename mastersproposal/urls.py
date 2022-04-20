from django.urls import path 
from django.urls import re_path as url
from . import views 

app_name = 'mastersproposal'

urlpatterns = [ 
    path('', views.home, name='home'), 
    url('about/', views.about, name='about'),
    url('proposals/', views.proposals, name='proposals'),
    url('thesis/', views.thesis, name='thesis'),
    url('services/', views.services, name='services'),
    url('thesis-format/', views.thesisformat, name='thesisformat'),
    url('topic/', views.topic, name='topic'),
    url('prices/', views.topic, name='prices'),
    url('order/', views.order, name='order'),
] 