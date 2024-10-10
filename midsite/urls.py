"""
URL configuration for midsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import ping
from core.views import Home
from core.views import First
from core.views import Login, form_submission
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("ping", ping),
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name='home'),
    path("start/", First.as_view(), name='start'),
    path('login/', Login.as_view(), name='login'),
    path('login/form_submission/', form_submission, name='Login.form_submission'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


