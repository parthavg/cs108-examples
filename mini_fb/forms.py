from django import forms
from .models import Profile, StatusMessage, Image


class CreateProfileForm(forms.ModelForm):
    '''A form to create a new profile object'''

class Meta:
        '''additional data about this form'''
        model = Profile
        fields = ['first_name', 'last_name','city', 'email_address']#which fields to create
        

class UpdateProfileForm(forms.ModelForm):
    '''Updates profile forms'''

class Meta: 
    '''additional data about this form'''
    model = Profile
    fields = ['city', 'email_address']

class CreateStatusMessageForm(forms.ModelForm):
    '''Creates Status Message forms'''

class Meta:
    '''additional data about this form'''
    model = StatusMessage
    fields = ['message']

class ImageField(forms.ModelForm):
    '''Allows to collect images from the user.'''

class Meta:
    '''additional data about the image of this form'''
    model = StatusMessage
    fields = ['image']