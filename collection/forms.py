from django import forms
from django.db import models
from collection.models import File

class FileForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file',
		help_text='max 42 megabytes'
		)

class InfoForm(forms.Form):
	class Meta:
		form = FileForm
		fields = ('name', 'description', 'price')