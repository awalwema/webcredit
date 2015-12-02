from django import forms
from django.forms import ModelForm
from collection.models import File
 
 
class FileFieldForm(ModelForm, forms.Form):
    def __init__(self, user,*args, **kwargs):
        super(FileFieldForm, self).__init__(*args, **kwargs)
 
    class Meta:
        model = File
        fields = ('name', 'description', 'price',)
    docfile = forms.FileField(
            label='Select a file',
            help_text='max 42 megabytes',)
 
 
    
