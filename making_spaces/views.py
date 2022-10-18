from re import template
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'index.html'
    return render(request, template_name)

def about(request):
    template_name = 'about.html'
    return render(request, template_name)

def services(request):
    template_name = 'services.html'
    return render(request, template_name)

def projects(request):
    template_name = 'projects.html'
    return render(request, template_name)

def blog(request):
    template_name = 'blog.html'
    return render(request, template_name)

def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)



