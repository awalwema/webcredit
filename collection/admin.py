from django.contrib import admin

# Register your models here.
from collection.models import File
from collection.models import UserProfile
from collection.models import Transaction


#set up automated slug creation
class FileAdmin(admin.ModelAdmin):
	model = File
	list_display = ('name', 'description','price', 'docfile')
	prepopulated_fields = {'slug': ('name',)}

class UserProfileAdmin(admin.ModelAdmin):
	model = UserProfile
	list_display = ('user','first_name','last_name','balance')

class TransactionAdmin(admin.ModelAdmin):
	model = UserProfile
	list_display = ('user','amount')

	    
	
admin.site.register(File, FileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Transaction, TransactionAdmin)
		
