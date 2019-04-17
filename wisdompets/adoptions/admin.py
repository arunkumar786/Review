from django.contrib import admin

# Register your models here.

from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	 # here admin have list display
	 # so we are using that.
	 # here we are listing the table columns
	 # from the models.py
	 list_display = ['name', 'species', 'breed', 'age', 'sex']
	 # here in django, by default, model instances
	 # are viewed in admin or shell as model name objects
	 # so if we overide the default method which is 
	 # __str__ then instance names will be visible.