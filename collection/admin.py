from django.contrib import admin

# Register your models here.
from collection.models import File



#set up automated slug creation
class FileAdmin(admin.ModelAdmin):
	model = File
	list_display = ('name', 'description','price', 'f')
	prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(File, FileAdmin)
		
