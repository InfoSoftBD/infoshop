from django.contrib import admin
from .models import CustomerInfo

# Register your models here.

@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email', 'slug', 'telephone', 'address', 'postal_code','city','country','created','updated')
	list_filter = ('last_name','postal_code','city','country','created','updated')
	search_fields = ('first_name','last_name','email', 'slug', 'telephone', 'address', 'postal_code','city','country','created','updated')
	prepopulated_fields = {'slug': ('email',)}