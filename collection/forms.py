from django import forms
from django.forms import ModelForm
from collection.models import File

class FileForm(forms.Form):
	docfile = forms.FileField(
	label='Select a file',
	help_text='max 42 megabytes',)

class FileFieldForm(ModelForm, forms.Form):
	class Meta:
		model = File
		fields = ('name', 'description', 'price',)
	docfile = forms.FileField(
	        label='Select a file',
	        help_text='max 42 megabytes',)			

	