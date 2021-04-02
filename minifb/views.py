from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote
import random


class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Quote #retrieve quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"

class QuotePageView(DetailView):
    '''Dispaly a single quote object.'''
    model = Quote #retrieve quote objects from the database
    template_name = "quotes/quote.html"
    context_object_name = "quote"

class RandomQuotePageView(DetailView):
    '''Dispaly a single quote object.'''
    model = Quote #retrieve quote objects from the database
    template_name = "quotes/quote.html"
    context_object_name = "quote"

    def get_object(self):
        '''Select one quote at random for display in the quote.html template.'''

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()
        # select one at random 
        q = random.choice(quotes)
        return q
# Create your views here.
