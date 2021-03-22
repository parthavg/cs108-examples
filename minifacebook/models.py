from django.db import models

# Create your models here.


class Quote(models.Model):
    "Access to all data fields"

    text = models.TextField(blank=True)
    author = models.TextField(blank=True)

    def __str__(self):
        '''Return a f string'''

        return f'{self.text} - {self.author}'