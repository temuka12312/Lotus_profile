from django.contrib import admin
from core.models import PersonInfo

# Register your models here.

class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'gmail')
    search_fields = ('name', 'gmail', 'phone')

admin.site.register(PersonInfo, PersonInfoAdmin)
