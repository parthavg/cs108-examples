# file name: project/forms.py
# author: Parthav Gupta
# email: parthavg@bu.edu
# description: allows the user to add additional data in the form of create,update and delete into the 
# pre-existing data provided in the project admin database.

from django import forms
from .models import *


CATEGORY_CHOICES= [
    ('vintage', 'Vintages'),
    ('modern', 'Moderns'),
    ('classic', 'Classics'),
    ] 


class CreateListingForm(forms.ModelForm):
        '''A form to create a new poster object.'''#allows user to upload new Poster in database
        tittle = forms.CharField(label='Title',required=True)#imported from the Poster model to display 
        actual_price = forms.CharField(label='Actual Price',required=True)#imported from the Poster model to display 
        discounted_price = forms.CharField(label='Discounted Price',required=True)#imported from the Poster model to display 
        poster_image_url = forms.URLField(label='Poster Image',required=True)#imported from the Poster model to display 
        description = forms.CharField(label='Description',required=True)#imported from the Poster model to display 
        category= forms.CharField(label='What category does the poster fall under?', widget=forms.Select(choices=CATEGORY_CHOICES))#imported from the Poster model to display 
        class Meta:
            '''additional data about this form'''
            model = Poster
            fields = ['tittle', 'actual_price','discounted_price','poster_image_url', 'description', 'category']#which fields to create

class CreateProfileForm(forms.ModelForm):#allows user to add new Profile in database
        '''A form to create a new profile object.'''
        name = forms.CharField(label='first name',required=True)#imported from the Profile model to display 
        email_address = forms.CharField(label='last name', required=True)#imported from the Profile model to display 
        profile_image_url = forms.URLField(label='profile_image_url', required=True)#imported from the Profile model to display 
        class Meta:
            '''additional data about this form'''
            model = Profile
            fields = ['name', 'email_address', 'profile_image_url']#which fields to create
        

class CreateReviewForm(forms.ModelForm):#allows user to upload new Review in database linked to Profile
        '''A form to create a new review object'''
        message = forms.CharField(label='message',required=True)#imported from the Review model to display
        #time_stamp = forms.CharField(label='time_stamp',required=True)
        

        class Meta:
            '''additional data about this form'''
            model = Review
            fields = ['message', 'profile'] #which fields to create



class UpdatePosterForm(forms.ModelForm):#allows user to update existing Poster in database
        '''A form to update the existing Poster object'''
        tittle = forms.CharField(label='Title',required=True)#imported from the Poster model to display 
        actual_price = forms.CharField(label='Actual Price',required=True)#imported from the Poster model to display 
        discounted_price = forms.CharField(label='Discounted Price',required=True)#imported from the Poster model to display 
        poster_image_url = forms.URLField(label='Poster Image',required=True)#imported from the Poster model to display 
        description = forms.CharField(label='Description',required=True)#imported from the Poster model to display 
        category= forms.CharField(label='What category does the poster fall under?', widget=forms.Select(choices=CATEGORY_CHOICES))#imported from the Poster model to display 
        class Meta:
            '''additional data about this form'''
            model = Poster
            fields = ['tittle', 'actual_price','discounted_price','poster_image_url', 'description', 'category']#which fields to create


