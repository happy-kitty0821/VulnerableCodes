from django.shortcuts import render, redirect
from .models import Feedbacks
from django.contrib import messages
# Create your views here.
def homePage(request):
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

def products(request):
    return render(request, 'products.html')

def moreProducts(request):
    return render(request, 'moreproducts.html')

def feedbacks(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        print(f"username : {username} email: {email} contact: {contact} message: {message}")
        feedback = Feedbacks(username=username, email=email, contact=contact, message=message)
        feedback.save()
    return render(request, 'feedback.html')
