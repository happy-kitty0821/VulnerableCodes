from django.shortcuts import render, redirect
from .models import Feedbacks
from django.contrib import messages
from django.shortcuts import render
from .models import User
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def moreProducts(request):
    return render(request, 'moreproducts.html')



# def login(request):
#     if request.method == 'POST':
#         input_username = request.POST.get('username')
#         input_password = request.POST.get('password')
#         username = input_username
#         password = input_password
#         print(f"username : {username} and password : {password}")

#         # Vulnerable SQLite query with string interpolation
#         query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"
#         print(f"SQL query: {query}")

#         # Execute the vulnerable query
#         with connection.cursor() as cursor:
#             cursor.execute(query)
#             result = cursor.fetchall()
#             print(f"result: {result}")

#         if result:
#             # Fetch all users from the User model
#             users = User.objects.all()
#             # Authentication successful (for educational purposes only!)
#             return render(request, 'admin.html', {'user': result[0], 'users': users})
#         else:
#             # Authentication failed
#             return HttpResponse('<h1>Username or password failed</h1>')

#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')

        # Intentionally vulnerable SQL query (for educational purposes only!)
        query = f"SELECT * FROM auth_user WHERE username = '{input_username}' AND password = '{input_password}'"

        # Execute the vulnerable query
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        if result:
            return render(request, 'admin.html', {'user': result[0]})
        else:
            #authentication failed
            return HttpResponse('<h1>Username or password failed</h1>')

    return render(request, 'login.html')

def customerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('custusername')
        password = request.POST.get('custpassword')
        print(f"username: {username} and password:{password}")
        query = f"SELECT * FROM loginapp_user WHERE username = '{username}' AND password = '{password}'"
        print(f"sql query for customer login is {query}")
        # Execute the vulnerable query
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"result: {result}")
        if result:
            return JsonResponse({'success': True, 'message': 'Login Success Here is the flag:IIC_CTF{UseEncryptionInPassword}'})
        else:
            # Authentication failed
             return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    return render(request, 'customerLogin.html')


def customerReg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profilePic')
        print(f"user registration credentials 1. Username {username} 2. Password:{password}")
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'customerReg.html', {'error': 'Username already taken'})
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return render(request, 'customerReg.html', {'error': 'Email already registered'})
        # Check if the contact is already registered
        if User.objects.filter(contact=contact).exists():
            return render(request, 'customerReg.html', {'error': 'Contact already registered'})
        # If no duplicates found, create and save the new customer
        new_customer = User(
            username=username,
            email=email,
            contact=contact,
            password=password,
             profilePic=profile_pic
        )
        new_customer.save()

        return redirect('customerLogin')  # Redirect to the login page after successful registration

    return render(request, 'customerReg.html')

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

# def showUploadedPic(request):
#     # Retrieve all users with profile pictures
#     users_with_profile_pic = User.objects.exclude(profilePic__isnull=True).exclude(profilePic__exact='')
#     context = {
#         'users_with_profile_pic': users_with_profile_pic
#     }
#     return render(request, 'uploads.html', context)

import os
from django.conf import settings
def showUploadedPic(request):
    # Define the path to the profile pictures directory
    profile_pic_dir = os.path.join(settings.MEDIA_ROOT, 'profilePics')
    # Get a list of all files in the directory
    profile_pic_files = os.listdir(profile_pic_dir)
    # Generate URLs for the images
    profile_pic_urls = [os.path.join(settings.MEDIA_URL, 'profilePics', file) for file in profile_pic_files]
    # Zip the lists
    profile_pic_data = zip(profile_pic_files, profile_pic_urls)
    context = {
        'profile_pic_data': profile_pic_data
    }

    return render(request, 'uploads.html', context)
