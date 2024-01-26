from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html')


from django.shortcuts import render
from .models import User

def login(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']

        user = User()
        result = user.authenticate_user(input_username, input_password)

        if result:
            # Authentication successful
            return render(request, 'success.html')
        else:
            # Authentication failed
            return render(request, 'failure.html')
    return render(request, 'login.html')
