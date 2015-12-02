from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, default = 'john')
	firstname = models.CharField(max_length=40, default = 'john')
	lastname = models.CharField(max_length=50, default = 'doe')
	email = models.EmailField(default = 'johndoe@gmail.com')
	balance = models.DecimalField(max_digits=7,decimal_places=2, default = 100)

	def __str__(self):
		return "%s's profile" % self.user  

	# User
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			profile, created = UserProfile.objects.get_or_create(user=instance)  

	def __unicode__(self):
		return unicode(self.user.username)

class File(models.Model):
	"""This holds a single user uploaded file"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=7,decimal_places=2)
	docfile = models.FileField(upload_to='files/%Y/%m/%d')
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(UserProfile)

class Transaction(models.Model):
	user = models.ForeignKey(UserProfile)
	amount = models.DecimalField(max_digits=7,decimal_places=2, default = 0)

	def save(self, *args, **kwargs):
		self.user.balance = self.user.balance + self.amount
		super(Transaction, self).save(*args, **kwargs)
		self.user.save()
		


