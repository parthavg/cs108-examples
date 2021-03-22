from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    '''A specialized verison of Template view'''

    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    '''A specialized verison of Template view'''

    template_name = "pages/about.html"

class SchedulePageView(TemplateView):
    '''A specialized verison of Schedule view'''

    template_name = "pages/schedule.html"