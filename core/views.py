from django.shortcuts import render
import os
import json
import logging

from django.http import JsonResponse

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from core.models import PersonInfo
from core.models import Register
from django.contrib.auth import authenticate, login


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
        context['information'] = PersonInfo.objects.filter()
        return context


class Login(TemplateView):
    template_name = "login/signup.html"

# Move form_submission outside of the class
@csrf_exempt
def sign_in_submission(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)  # Log the user in
            return JsonResponse({'status': 'success', 'message': 'Logged in successfully', 'redirect_url': '/dashboard/'})  # Change the URL to the desired page
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})


def sign_up_submission(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")
            phone = data.get("phone")

            users = Register.objects.create(
                username=name,
                email=email,
                phone=phone,
                password=(password),  # Hash the password
            )
            users.save()

            return JsonResponse({"status": "success", "message": "User registered successfully."})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method."})
