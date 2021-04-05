from django.db import models
from django.urls import reverse
import random

# Create your models here.

class Person(models.Model):
    '''Represent a Person who said something notable'''

    name = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of person'''
        return self.name
    
    def get_random_image(self):
        '''Return an image of this person, selected at random'''

        images = Image.objects.filter(person=self)

        # select one at random to return
        return random.choice(images)



class Quote(models.Model):
    "Represents a quote by a famous person. "

    # data attributes:
    text = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    #author = models.TextField(blank=True)
    #image_url = models.URLField(blank=True)

    def _str_(self):
        '''Return a string representation of this quote.'''

        return f'"{self.text}" - {self.person}'
    
    def get__absolute_url(self): #Assignment 18
        '''Provide a URL to show this object'''

        #'quote/<int:pk>'
        return reverse('quote', kwargs={'pk':self.pk})
        
class Image(models.Model):
    '''Represent an image URL for a person.'''
    image_url = models.URLField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        '''Return the image URL of this Image'''
        return self.image_url

