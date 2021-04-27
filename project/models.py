from django.db import models
from django.urls import reverse
from .models import *

# Create your models here.
CATEGORY_CHOICES = [ 
        ("vintage",'Vintages'),
        ("modern",'Moderns'),
        ("classic",'Classics')
     ]

class Profile(models.Model):
    '''Represents the details of a user'''

    #data attributes
    name = models.TextField(blank=True)
    email_id = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self") 
    
    def __str__(self):
        return f'"{self.name}"'

    def get_review(self):
        '''Return a review uploaded by this profile.'''

        # find all reviews for this profile
        return Review.objects.filter(profile=self)

    def get_friends(self):
        '''Return all friends for this profile'''
        return self.friends.all()


class Poster(models.Model):
    '''Represents the attributes of a poster'''

    #data attributes 
    tittle = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    poster_image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100,choices = CATEGORY_CHOICES) 

    def __str__(self):
        return f'"{self.tittle}" - "{self.price}" - "{self.poster_image_url}" - "{self.description}" - "{self.category}"'

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

    message = models.TextField(blank=True)
    time_stamp = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey('Poster', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.message}" - "{self.time_stamp}"'




    

    








