from django.db import models

# Create your models here.

class Quote(models.Model):
    "Represents a quote by a famous person. "

    # data attributes:
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)

    def _str_(self):
        '''Return a string representation of this quote.'''

        return f'{self.text} - {self.author}'
        
