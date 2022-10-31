from msilib.schema import Error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import contactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    contact_form = contactForm()
    template_name = 'index.html'
    if request.method == 'GET':
        context = {
            'form': contact_form
        }
        return render(request, template_name, context)
    else:
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid():
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            telefono = request.POST.get('telefono')
            mensaje = request.POST.get('mensaje')

            email = EmailMessage(
                'Nuevo correo',
                'Usuario: {}\n Correo: {}\n Mensaje: {}\n'.format(
                    nombre, correo, mensaje),
                f'{correo}',
                [settings.EMAIL_HOST_USER],
            )
            try:
                email.send(fail_silently=False)
                messages.add_message(request=request, level=messages.SUCCESS,
                                     message="Gracias por comunicarte con nosotros")
            except:
                messages.add_message(request=request, level=messages.ERROR,
                                     message="Opps!, hubo un error al enviar tu mensaje")
                return redirect('/home/')
    context = {
        'form': contact_form
    }
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
