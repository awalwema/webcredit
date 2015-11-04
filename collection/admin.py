from django.contrib import admin

# Register your models here.
from collection.models import File
from collection.models import Wallet



#set up automated slug creation
class FileAdmin(admin.ModelAdmin):
	model = File
	list_display = ('name', 'description','price', 'docfile')
	prepopulated_fields = {'slug': ('name',)}

class WalletAdmin(admin.ModelAdmin):
	model = Wallet
	list_display = ('user','balance')
	    
	
admin.site.register(File, FileAdmin)
admin.site.register(Wallet, WalletAdmin)
		
