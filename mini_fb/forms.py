from django import forms
from .models import Profile, StatusMessage, Image


class CreateProfileForm(forms.ModelForm):
    '''A form to create a new profile object'''
    first_name = forms.CharField(label='first name',required=True)
    last_name = forms.CharField(label='last name', required=True)
    city = forms.CharField(label='last name', required=True)
    email_address = forms.CharField(label='last name', required=True)
    profile_image_url = forms.URLField(label='profile_image_url', required=True)
    class Meta:
        '''additional data about this form'''
        model = Profile
        fields = ['first_name', 'last_name','city', 'email_address', 'profile_image_url']#which fields to create
        

class UpdateProfileForm(forms.ModelForm):
    '''Updates profile forms'''
    city = forms.CharField(label='last name', required=True)
    email_address = forms.CharField(label='last name', required=True)
    profile_image_url = forms.URLField(label='profile_image_url', required=True)
    class Meta: 
        '''additional data about this form'''
        model = Profile
        fields = ['city', 'email_address', 'profile_image_url']


class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create new status message forms'''
    time_stamp = forms.TimeField(label='time_stamp', required=True)
    image = forms.ImageField(label='image', required=False)

    class Meta:
        model = StatusMessage
        fields = ['message', 'image', 'time_stamp']
