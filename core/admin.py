from django.contrib import admin
from core.models import PersonInfo, Register
from core.models import Game
from core.models import Software


class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('email',) 
    ordering = ('name',)  

admin.site.register(PersonInfo, PersonInfoAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email',)
    search_fields = ('username', 'email', 'phone',)
    list_filter = ('email',)  
    ordering = ('username',)  

admin.site.register(Register, RegisterAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'download_link', 'game_img',)
    search_fields = ('game_name', 'download_link', 'game_img',)
    list_filter = ('game_name',)  
    ordering = ('game_name',)  

admin.site.register(Game, GameAdmin)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'description',)
    search_fields = ('title', 'img', 'description',)
    list_filter = ('title',)  
    ordering = ('title',)  

admin.site.register(Software, SoftwareAdmin)
