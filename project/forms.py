from django import forms
from .models import *


CATEGORY_CHOICES= [
    ('vintage', 'Vintages'),
    ('modern', 'Moderns'),
    ('classic', 'Classics'),
    ]
class CreateListingForm(forms.ModelForm):
        '''A form to create a new poster object.'''
        tittle = forms.CharField(label='tittle',required=True)
        price = forms.CharField(label='price',required=True)
        poster_image_url = forms.URLField(label='poster_image_url',required=True)
        description = forms.CharField(label='description',required=True)
        category= forms.CharField(label='What category does the poster fall under?', widget=forms.Select(choices=CATEGORY_CHOICES))
        class Meta:
            '''additional data about this form'''
            model = Poster
            fields = ['tittle', 'price','poster_image_url', 'description', 'category']#which fields to create

class CreateProfileForm(forms.ModelForm):
        '''A form to create a new profile object.'''
        name = forms.CharField(label='first name',required=True)
        email_address = forms.CharField(label='last name', required=True)
        profile_image_url = forms.URLField(label='profile_image_url', required=True)
        class Meta:
            '''additional data about this form'''
            model = Profile
            fields = ['name', 'email_address', 'profile_image_url']#which fields to create
        

class CreateReviewForm(forms.ModelForm):
        '''A form to create a new review object'''
        message = forms.CharField(label='message',required=True)
        #time_stamp = forms.CharField(label='time_stamp',required=True)
        

        class Meta:
            '''additional data about this form'''
            model = Review
            fields = ['message', 'profile'] #which fields to create



class UpdatePosterForm(forms.ModelForm):
        '''A form to update the existing Poster object'''
        tittle = forms.CharField(label='tittle',required=True)
        price = forms.CharField(label='price',required=True)
        poster_image_url = forms.URLField(label='poster_image_url',required=True)
        description = forms.CharField(label='description',required=True)
        category= forms.CharField(label='What category does the poster fall under?', widget=forms.Select(choices=CATEGORY_CHOICES))
        class Meta:
            '''additional data about this form'''
            model = Poster
            fields = ['tittle', 'price','poster_image_url', 'description', 'category']#which fields to create


