from django.contrib import admin
from core.models import PersonInfo, Register
from core.models import Game
from core.models import Software
# from core.models import Userflug
# from core.models import Report_offer


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

# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('reporter_name', 'report', 'reporter_offer',)
#     search_fields = ('reporter_name', 'report', 'reporter_offer',)
#     list_filter = ('reporter_name',)  
#     ordering = ('reporter_name',) 

# admin.site.register(Report_offer, ReportAdmin) 

# class UserflugAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'user_role', 'user_profile',)
#     search_fields = ('user_name', 'user_role', 'user_profile',)
#     list_filter = ('user_name',)  
#     ordering = ('user_name',) 

# admin.site.register(Userflug, UserflugAdmin)
