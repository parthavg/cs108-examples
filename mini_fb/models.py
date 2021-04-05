from django.db import models
import random
from django.urls import reverse
from .models import *

# Create your models here.

class Profile(models.Model):
    '''Show the profile of an individual'''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    email_address = models.CharField(max_length=45)
    #profile_image_url = models.URLField(blank=True)

def __str__(self):
        return f'"{self.first_name}" - "{self.last_name}" - "{self.city}" - "{self.email_address}"'

def get__absolute_url(self): #Assignment 18
        '''Provide a URL to show this object'''

        #'show_profile_page/<int:pk>'
        return reverse('profile', kwargs={'pk':self.pk})



class StatusMessage(models.Model):
    '''Model Data attributes of Facebook Status Message'''
    time_stamp = models.TextField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True) 
    

def __str__(self):
        return f'"{self.time_stamp}" - "{self.message}" - "{self.profile}"'

class Image(models.Model):
    profile_image_url = models.URLField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

def __str__(self):
    "return the image url of this image"
    return self.profile_image_url