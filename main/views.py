from django.shortcuts import render, redirect
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
            subject = form.cleaned_data['subject']
            F_name  = form.cleaned_data['F_name']
            L_name  = form.cleaned_data['L_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['kipkoechk38@gmail.com'])
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
            course = form.cleaned_data['course']
            F_name  = form.cleaned_data['F_name']
            M_name  = form.cleaned_data['M_name']
            S_name  = form.cleaned_data['S_name']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_num']
            message = form.cleaned_data['message']
            try:
                send_mail(course, message, email, ['kipkoechk38@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success') 
    return render(request, template, {'form':form})

def services(request):
    template = 'services.html'
    return render(request, template, { })

def base(request):
    template = 'base.html'
    return render(request, template, { })

def blog(request):
    template = 'blog/home.html'
    return render(request, template, { })
