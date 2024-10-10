from django.shortcuts import render
import os
import json
import logging

from django.http import JsonResponse

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from core.models import PersonInfo
from core.models import Register


def ping(request):
    data = {}
    data['build_mode'] = os.environ.get("BUILD_MODE")
    data['build_date'] = os.environ.get("BUILD_DATE")
    data['version'] = os.environ.get("IMAGE_VERSION")
    data['app'] = "core"
    return JsonResponse(data)


class Home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["information"] = PersonInfo.objects.all()
        return context
    
class First(TemplateView):
    template_name = "first.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = PersonInfo.objects.filter()
        return context


class Login(TemplateView):
    template_name = "login/signup.html"

# Move form_submission outside of the class
@csrf_exempt
def form_submission(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})
    
    data = json.loads(request.body)
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    
    Register.objects.create(name=name, email=email, phone=phone)

    return JsonResponse({'status': 'success'})