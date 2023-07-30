from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class contactPageView(TemplateView):
    template_name = 'pages/contact.html'
    

def services(request):
    return render(request,'pages/services.html')