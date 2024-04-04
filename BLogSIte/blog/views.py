from django.utils.text import slugify
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, normUser, Comment, feedbacks
from django.contrib.auth import logout as django_logout
import time, os
from datetime import datetime
from django.conf import settings


def robots(request):
    # Define the contents of your robots.txt file
    robots_txt = """
   User-agent: *
        Disallow: /admin/
        Disallow: /loginusr/
        Disallow: /logout/
        Disallow: /loginusr/signup/
        Disallow: /profile/
        Disallow: /profile/writeBlog/
        Disallow: /development

        # Note: for development purposes only
        # Note: to the dev ops team robots.txt can sometimes reveal sensitive information. 
        # Note : from the development team please ensure that the robots.txt is removed in production or it does not expose any confidential URLs or directories. 

        # Robots.txt Vulnerability:
        # Sensitive Information Exposure: Developers might inadvertently include sensitive URLs or directories in the robots.txt file, which is meant to control search engine crawlers' access to website content.
        # Security by Obscurity: Relying on robots.txt to hide sensitive information is a form of security by obscurity, which is generally not recommended as a primary security measure.
        # Discovery of Hidden Resources: Attackers can use robots.txt to discover hidden or restricted resources, such as admin panels, development environments, or backup files, that were not meant to be exposed.
        # Potential for Information Leakage: Exposing internal paths or directories through robots.txt can provide attackers with valuable information about the structure and layout of the web application, aiding them in crafting more targeted attacks.
        # Mitigation: Developers should carefully review and ensure that robots.txt does not expose any confidential or sensitive URLs. It's also essential to implement proper access controls and security measures within the application itself rather than relying solely on robots.txt for security. Additionally, regular security audits can help identify and mitigate such vulnerabilities.

        flag: IIC_CTF{eXp0seD r0b0t$.t*+}
    """
    #return the robots.txt content with the appropriate content type
    return HttpResponse(robots_txt, content_type='text/plain')

def userlogin(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        # Intentionally vulnerable SQL query (for educational purposes only!)
        query = f"SELECT * FROM blog_normUser WHERE username = '{input_username}' AND password = '{input_password}'"
        print(f'query: {query}')
        # Execute the vulnerable query
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        if result:
           # Redirect to profile page upon successful login
            print("Login successful. Redirecting to profile page.")
            messages.success(request, "Login Sucess full here is the flag IIC_CTF{You_Got_tHe_flag_using_SQLI??}")
            return redirect('profile')
        else:
            # Login failed
            messages.error(request, 'Login failed. Please check your username and password.')
            return redirect('loginusr')  # Redirect back to the login page
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profilePic = request.POST.get('profilePic')
        password = request.POST.get('password')
        securityQuestion = request.POST.get('securityQuestion')
        secAnswer = request.POST.get('secAnswer')
        print(f"username = {username} email = {email} phone = {phone} password = {password}")
        # Check if the username is already taken
        # if normUser.objects.filter(username=username).exists():
        #     messages.error(request, 'username already occupied!!!')
        # # Check if the email is already registered
        # if normUser.objects.filter(email=email).exists():
        #     messages.error(request, 'email aready used!!!')
        # # Check if the contact is already registered
        # if normUser.objects.filter(phone=phone).exists():
        #    messages.error(request, 'contact already registered!!!')
        # If no duplicates found, create and save the new customer
        newUser = normUser(
            username=username,
            email=email,
            phone=phone,
            password=password,
            profilePic=profilePic,
            securityQuestion = securityQuestion,
            secAnswer= secAnswer
        )
        newUser.save()
        messages.success(request, 'User created sucessfully!!!')
        time.sleep(4)
        return redirect('loginusr')  # Redirect to the login page after successful registration
    return render(request, 'signup.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = reverse_lazy('loginusr')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect('loginusr')
        comment_content = request.POST.get('comment')
        if comment_content:
            comment = Comment.objects.create(post=self.object, user=request.user, content=comment_content)
            messages.success(request, 'Your comment has been posted successfully.')
        return redirect('post_detail', slug=self.object.slug)
    


def writeBlogPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        author = request.user
        
        # Generate a unique slug based on the title
        slug = slugify(title)
        
        # Check if the generated slug already exists, and if so, append a counter to make it unique
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{slug}-{counter}"
            counter += 1
        # Create the post with the unique slug
        post = Post.objects.create(
            title=title,
            content=content,
            status=status,
            author=author,
            slug=slug
        )
        # Set a success message
        messages.success(request, 'Your blog post has been submitted successfully.')
        # Redirect to the home page
        return redirect('home')
    # If the request method is GET, just render the form template
    return render(request, 'writeblog.html')

def profile(request):
    username = request.POST.get('username')  # Fetch the username entered during login
    user = normUser.objects.get(username=username)  # Fetch the normUser object using username
    posts = Post.objects.filter(status=1).order_by('-created_on')  # Fetch all published posts
    return render(request, 'profile.html', {'user': user, 'posts': posts})  # Pass user and posts to the template context

def logout(request):
    django_logout(request)
    return redirect('home')



def about(request):
    current_time = datetime.now()
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        if feedback_text:
            # Save to database
            feedback = feedbacks(content=feedback_text, created_at=current_time)
            feedback.save()

            # Save to text file
            file_path = os.path.join(settings.MEDIA_ROOT, 'feedbacks', 'feedbacks.txt')
            with open(file_path, 'a') as f:
                f.write(f'{feedback_text}\n')

            messages.success(request, 'Feedback submitted successfully.')
            return redirect('about')
        else:
            messages.error(request, 'Feedback cannot be empty.')
            return redirect('about')  # Return a redirect here if the feedback is empty
    #send feedbacks to the aboutus.html page
    all_feedbacks = feedbacks.objects.all()
    return render(request, 'aboutus.html',  {'all_feedbacks': all_feedbacks})

def getFlag(request):
    # Check if the request is AJAX
    if request.is_ajax():
        # Generate the flag here (replace this with your flag generation logic)
        flag = "IIC_CTF{XSS_Vulnerability!!}"

        # Return the flag as a JSON response
        return JsonResponse({'flag': flag})

    # If the request is not AJAX, return a 404 error
    else:
        return JsonResponse({'error': 'Page not found'}, status=404)
    
def read_file(request):
    file_path = request.GET.get('file_path', '')
    file_content = ''
    if file_path:
        try:
            with open(os.path.join('media', file_path), 'r') as file:
                file_content = file.read()
        except FileNotFoundError:
            file_content = 'File not found'
    return render(request, 'aboutus.html', {'file_path': file_path, 'file_content': file_content})
    
def development(request):
    return render(request, 'development.html')