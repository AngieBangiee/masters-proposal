from django.urls import path 
from django.urls import re_path as url
from . import views 

app_name = 'mastersproposal'

urlpatterns = [ 
    path('', views.home, name='home'), 
    url('about/', views.about, name='about'),
    url('masters-proposals/', views.proposals, name='proposals'),
    url('masters-thesis/', views.thesis, name='thesis'),
    url('services/', views.services, name='services'),
    url('theses-format/', views.thesesformat, name='thesesformat'),
    url('topic/', views.topic, name='topic'),
    url('prices/', views.prices, name='prices'),
    url('order/', views.order, name='order'),
] 