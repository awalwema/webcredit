from django import forms
from django.forms import ModelForm
from collection.models import File

class FileForm(forms.Form):
	docfile = forms.FileField(
	label='Select a file',
	help_text='max 42 megabytes',)

class FileFieldForm(ModelForm, forms.Form):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(FileFieldForm, self).__init__(*args, **kwargs)

	class Meta:
		model = File
		fields = ('name', 'description', 'price',)
	docfile = forms.FileField(
	        label='Select a file',
	        help_text='max 42 megabytes',)
	def save(self, force_insert=False, force_update=False, commit=True):
		instance = super(FileFieldForm, self).save(commit=False)
		if self.user:
			instance.user = self.user
		return instance.save()


	