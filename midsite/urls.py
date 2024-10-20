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
from django.urls import path, include
from core.views import ping
from core.views import Home
from core.views import First
from core.views import Login
from django.conf.urls.static import static
from django.conf import settings
from core.views import sign_in_submission
from core.views import sign_up_submission
from core.views import room
import debug_toolbar


urlpatterns = [
    path("ping", ping),
    path("admin/", admin.site.urls),
    path("", Login.as_view(), name='home'),
    path("login/start/", First.as_view(), name='start'),
    path('login/<pk>/', Home.as_view(), name='login'),
    path('sign-in/', sign_in_submission, name='sign_in_submission'),
    path('sign-up/', sign_up_submission, name='sign_up_submission'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('chat/<str:room_name>/', room, name='chat_room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


