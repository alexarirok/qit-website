from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from main.forms import ContactForm, ApplicationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    template = 'home.html'
    return render(request, template, { })

def about(request):
    template = 'about.html'
    return render(request, template, { })

def contact(request):
    template = 'contacts.html'
    if request.method == 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject']
            First_name  = form.cleaned_data['F_name']
            Surname  = form.cleaned_data['L_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, First_name, Surname, email, ['norahmiles2@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sucess') 
    return render(request, template, {'form':form})

def application(request):
    template = 'application.html'
    if request.method == 'POST':
        form = ApplicationForm()
    else:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            First_name = form.cleaned_data['F_name']
            Middle_name  = form.cleaned_data['M_name']
            Surname  = form.cleaned_data['S_name']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_num']
            course = form.cleaned_data['course']
            message = form.cleaned_data['message']
            try:
                send_mail(First_name, Middle_name, Surname, email, phone_num, course, message ['norahmiles2@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sucess') 
    return render(request, template, {'form':form})

def services(request):
    template = 'services.html'
    return render(request, template, { })

def trainings(request):
    template = 'courses.html'
    return render(request, template, { })

def base(request):
    template = 'base.html'
    return render(request, template, { })

def blog(request):
    template = 'blog/index.html'
    return render(request, template, { })
