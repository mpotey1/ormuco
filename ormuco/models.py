from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	name = models.CharField(max_length=200)
	favorite_color = models.CharField(max_length=200)
	animal = models.CharField(max_length=200)
