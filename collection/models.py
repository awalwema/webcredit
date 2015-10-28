from django.db import models

# Create your models here.
class File(models.Model):
	"""This holds a single user uploaded file"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=7,decimal_places=2)
	f = models.FileField(upload_to='.')
	slug = models.SlugField(unique=True)