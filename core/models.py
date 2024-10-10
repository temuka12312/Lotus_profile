from django.db import models
from django.utils import timezone
from django.urls import reverse

from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    last_updated_date = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True



class PersonInfo(BaseModel):
    name = models.CharField("Нэр", max_length=256)
    person_image = models.ImageField(verbose_name="Зураг", null=True, blank=True, upload_to="midsite/person-information")
    bio = models.TextField(verbose_name="bio")
    phone = models.IntegerField(verbose_name="Утасны дугаар")
    gmail = models.CharField(verbose_name="Gmail", max_length=100)
    
    class Meta:
        verbose_name = "Person information"
        verbose_name_plural = "Person information"
        
    def __str__(self) -> str:
        return self.name
    

class Register(BaseModel):
    name = models.CharField("Нэр*", max_length=255)
    email = models.EmailField(verbose_name="И-мэйл*", max_length=255)
    phone = models.CharField(verbose_name="Утасны дугаар*", max_length=50)
    
    class Meta:
        verbose_name = "login"
        verbose_name_plural = "login"
        
    def __str__(self) -> str:
        return self.name