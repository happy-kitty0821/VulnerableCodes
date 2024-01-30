from django.shortcuts import render, redirect
from .models import Feedbacks
from django.contrib import messages
from django.shortcuts import render
from .models import User
from django.db import connection

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def moreProducts(request):
    return render(request, 'moreproducts.html')


def login(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        username = input_username
        password = input_password
        print(f"username : {username} and password : {password}")
        # Vulnerable SQLite query with string interpolation
        query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"
        print(f"SQL query: {query}")
        # Execute the vulnerable query
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"result: {result}")

        return render(request, 'results.html', {'result': result})
    return render(request, 'login.html')

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
