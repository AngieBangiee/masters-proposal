from django.shortcuts import render
from .models import Page

def home(request):
    return render(request, 'mastersproposal/home.html') 

def about(request):
    return render(request, 'mastersproposal/about.html')  

def proposals(request):
    return render(request, 'mastersproposal/masters-proposals.html')

def thesis(request):
    return render(request, 'mastersproposal/masters-thesis.html')

def services(request):
    return render(request, 'mastersproposal/services.html')

def thesesformat(request):
    return render(request, 'mastersproposal/theses-format.html') 

def topic(request):
    return render(request, 'mastersproposal/topic.html') 

def prices(request):
    return render(request, 'mastersproposal/prices.html')

def order(request):
    return render(request, 'mastersproposal/order.html')

def pages(request, slug):
    slug = slug
    page = Page.objects.get(slug=slug)
    context = {
        'meta_title':page.meta_title,
        'meta_description':page.meta_description,
        'title':page.title,
        'content':page.content,  
    }
    return render(request, 'mastersproposal/page.html', context)
