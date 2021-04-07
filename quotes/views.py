from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Quote, Person
from.forms import CreateQuoteForm
import random


class HomePageView(ListView): 
    '''Show a listing of Quotes.'''
    model = Quote # retrieve Quote objects from the database
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

class PersonPageView(DetailView):
    '''Dispaly a single Person object.'''
    model = Person #retrieve quote objects from the database
    template_name = "quotes/person.html" # delegate the display to this template
    context_object_name = "person" # use this variable name in the template

class CreateQuoteView(CreateView):
    '''Create a new Quote object and store in database.'''

    form_class = CreateQuoteForm
    template_name = "quotes/create_quote_form.html"

