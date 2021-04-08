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
    profile_image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")


    def __str__(self):
        return f'"{self.first_name}" - "{self.last_name}" - "{self.city}" - "{self.email_address}" -"{self.profile_image_url}"'


    def get_status_messages(self):
        '''Return the status message for the profile'''

        return StatusMessage.objects.filter(profile=self)


    def get_absolute_url(self):
        '''Provide a URL to show the object'''

        #'profile/<int:pk>'
        return reverse('show_profile_page',kwargs={'pk':self.pk})
    
    def get_friends(self):
        '''Return all friends for this profile'''
        return self.friends.all()

    def get_news_feed(self):
        '''obtain and return the news feed items'''

        buddies = self.friends.all()
        news = StatusMessage.objects.filter(profile__in=buddies).order_by("-time_stamp")
        return news

    def get_friend_suggestions(self):
        '''shows a QuerySet of all Profile that could be added as friends'''

        possible_friends = Profile.objects.exclude(pk__in=self.get_friends())
        return possible_friends 

class StatusMessage(models.Model):
    '''Model Data attributes of Facebook Status Message'''
    time_stamp = models.TimeField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True) 

    def __str__(self):
         return f'"{self.time_stamp}" - "{self.message}" -"{self.image}"'

class Image(models.Model):
    profile_image_url = models.URLField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        "return the image url of this image"
        return self.profile_image_url







