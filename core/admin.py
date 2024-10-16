from django.contrib import admin
from core.models import PersonInfo, Register

# Register your models here.

class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('email',)  # Add filter by email
    ordering = ('name',)  # Default ordering by name

admin.site.register(PersonInfo, PersonInfoAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email',)
    search_fields = ('username', 'email', 'phone',)
    list_filter = ('email',)  # Add filter by email
    ordering = ('username',)  # Default ordering by name

admin.site.register(Register, RegisterAdmin)
