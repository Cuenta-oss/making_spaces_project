from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm

def home(request):
    contact_form = contactForm()
    context = {
        'form' : contact_form
    }
    template_name = 'index.html'
    print(contactForm)
    return render(request, template_name, context)

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

""" def send_mail_quote(request):
    context = {
        'form' : contactForm(),
    }
    return render(request, 'index.html', context) """