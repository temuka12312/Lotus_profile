from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from io import BytesIO
from django.core.files import File

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    last_updated_date = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True
    

class Register(BaseModel):
    username = models.CharField("Нэр*", max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name="И-мэйл*", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name="Утасны дугаар*", max_length=50, null=True, blank=True)
    password = models.CharField(verbose_name="password", max_length=400, null=True, blank=True)
    
    class Meta:
        verbose_name = "login"
        verbose_name_plural = "login"
        
    def __str__(self) -> str:
        return self.username
    
    
class PersonInfo(models.Model):
    name = models.CharField("Нэр", max_length=256)
    person_image = models.ImageField(verbose_name="Зураг", null=True, blank=True, upload_to="midsite/person-information")
    bio = models.TextField(verbose_name="bio")
    phone = models.IntegerField(verbose_name="Утасны дугаар")
    email = models.CharField(verbose_name="Gmail", max_length=100, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='person_info', null=True, blank=True)

    class Meta:
        verbose_name = "Person information"
        verbose_name_plural = "Person information"
    
    def __str__(self):
        return self.name
    
    
class Game(models.Model):
    game_name = models.CharField("Нэр", max_length=256)
    game_img = models.ImageField(verbose_name="Зураг", null=True, blank=True, upload_to="midsite/home/game_info")
    game_details = models.TextField(verbose_name="Заавар", null=True, blank=True)
    download_link = models.URLField(verbose_name="Тоглоомны холбоос", null=True, blank=True)
    
    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        
    def __str__(self):
        return self.game_name
    

class Software(models.Model):
    title = models.CharField("Гарчиг", max_length=256)
    description = models.TextField(verbose_name="Тайлбар", null=True, blank=True)
    img = models.ImageField(verbose_name="Зураг", null=True, blank=True, upload_to="midsite/home/software")
    link = models.URLField(verbose_name="Үсрэх url", null=True, blank=True)

    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"

    def __str__(self):
        return self.title


class ReportOffer(models.Model):
    user_name = models.CharField("user name", max_length=256)
    user_report = models.TextField(verbose_name= "user_reported", null=True, blank=True)
    user_proof = models.ImageField(verbose_name = "user_proof", null=True, blank=True, upload_to = "midsite/home/report")
    reported_page = models.URLField(verbose_name="reported_page_url", null=True, blank=True)

    class Meta:
        verbose_name = "user_report"
        verbose_name_plural = "user_reports"
    
    def __str__(self):
        return self.user_name

# class Userflug(models.Model):
#     user_name = models.CharField("Name", max_length=256)
#     user_profile = models.ImageField(verbose_name="Profile", null=True, blank=True, upload_to="midsite/home/user_profile")
#     user_role = models.TextField(verbose_name="Role", null=True, blank=True)
#     user_social_link = models.URLField(verbose_name="Social links", null=True, blank=True)

#     class Meta:
#         verbose_name = "user_roles"
#         verbose_name_plural = "user_roles"

#     def __str__(self):
#         return self.user_name
    
# class Report_offer(models.Model):
#     reporter_name = models.CharField("Reporter name", max_length=256)
#     reporter_offer = models.TextField(verbose_name= "Reporter offer", null=True, blank=True)
#     report = models.ImageField(verbose_name="Report", null=True, blank=True, upload_to="midsite/home/report")

#     class Meta:
#         verbose_name = "Report"
#         verbose_name_plural = "Report"

#     def __str__(self):
#         return self.reporter_name 