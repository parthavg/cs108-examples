# file name: project/admin.py
# author: Parthav Gupta
# email: parthavg@bu.edu
# description: is Django’s command-line utility for administrative tasks. 
# This document outlines all it can do.

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(Poster)
admin.site.register(Review)
