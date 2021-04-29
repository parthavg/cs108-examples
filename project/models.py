# file name: project/models.py
# author: Parthav Gupta
# email: parthavg@bu.edu
# description: this document helps create the structure for stored data including filed size, default values
# these are primarily Python objects

from django.db import models
from django.urls import reverse
from .models import *

# Create your models here.
CATEGORY_CHOICES = [ 
        ("vintage",'Vintages'),
        ("modern",'Moderns'),
        ("classic",'Classics')
      ]#Appears as a drop-down menu to give choice to user to categorize a poster 

GENRE_CHOICES = [
        ("Action",'Action'),
        ("Drama",'Drama'),
        ("Comedy",'Comedy'),
        ("Romance",'Romance'),
        ("Thrillers",'Thriller')
      ]#Appears as a drop-down menu to give choice to profile to choose favorite genre

class Profile(models.Model):
    '''Represents the details of a user'''

    #data attributes
    name = models.TextField(blank=True)
    email_id = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    fav_genre = models.CharField(max_length=100,choices = GENRE_CHOICES)
    friends = models.ManyToManyField("self") 
    
    def __str__(self):
        #returns the name to display as an attribute of Profile
        return f'"{self.name}"'


    def get_review(self):
        '''Returns a review uploaded by this profile.'''

        # find all reviews for this profile
        return Review.objects.filter(profile=self)

    def get_friends(self):
        '''Return all friends for this profile'''
        return self.friends.all()

    def get_friend_suggestions(self):
        '''shows a QuerySet of all Profile that could be added as friends'''

        possible_friends = Profile.objects.exclude(pk__in=self.get_friends())
        return possible_friends 

class Poster(models.Model):
    '''Represents the attributes of a poster'''

    #data attributes 
    tittle = models.TextField(blank=True)
    actual_price = models.IntegerField(blank=True)
    discounted_price = models.IntegerField(blank=True)
    poster_image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100,choices = CATEGORY_CHOICES) 

    def __str__(self):
        #returns all data attributes except the actual price
        return f'"{self.tittle}" - "{self.discounted_price}" - "{self.poster_image_url}" - "{self.description}" - "{self.category}"'

    def get_absolute_url(self):
        '''Provide a URL to show the poster object'''

        # reverse back to the show individual poster page 
        return reverse('show_poster_page',kwargs={'pk':self.pk})

    def get_review(self):
        '''Return a review uploaded for this poster'''

        # find all reviews for this poster
        return Review.objects.filter(poster=self)


class Review(models.Model):
    '''Represents the user reviews of those profiles that have purchased the poster'''
    
    #data attributes
    message = models.TextField(blank=True)
    time_stamp = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey('Poster', on_delete=models.CASCADE)#foreign key relationship to establish link with Poster model
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)#foreign key relationship to establish link with Profile model

    def __str__(self):
        #returns the message and time stamp to display as attributes of Review model
        return f'"{self.message}" - "{self.time_stamp}"'








    

    








