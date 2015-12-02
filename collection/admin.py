from django.contrib import admin

# Register your models here.
from collection.models import File
from collection.models import UserProfile


#set up automated slug creation
class FileAdmin(admin.ModelAdmin):
	model = File
	list_display = ('name', 'description','price', 'docfile')
	prepopulated_fields = {'slug': ('name',)}

class UserProfileAdmin(admin.ModelAdmin):
	model = UserProfile
	list_display = ('user','firstname','lastname','email','balance')

	    
	
admin.site.register(File, FileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
		
