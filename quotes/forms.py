from django import forms
from .models import Quote 


class CreateQuoteForm(forms.ModelForm):
    '''A form to create a new quote object'''
    
    class Meta:
        '''additional data about this form'''
        model = Quote
        fields = ['text','person']#which fields to create 