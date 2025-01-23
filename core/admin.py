from django.contrib import admin
from core.models import PersonInfo, Register
from core.models import Game

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

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'download_link', 'game_img',)
    search_fields = ('game_name', 'download_link', 'game_img',)
    list_filter = ('game_name',)  # Add filter by email
    ordering = ('game_name',)  # Default ordering by name

admin.site.register(Game, GameAdmin)
