
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class normUser(models.Model):
    userId = models.IntegerField(primary_key=True, null=False, unique=True, default=None)
    username = models.CharField(max_length=55, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone = models.IntegerField(unique=True, null=False)
    fullname = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
    profilePic = models.ImageField(null=True, upload_to='media/profilePics/')
    securityQuestion = models.TextField(max_length=60, null=False)
    secAnswer = models.TextField(max_length=55, null=False)

    def __str__(self):
        return self.username

class feedbacks(models.Model):
    content = models.TextField(default="this is the default message")
    annonuser = models.TextField(default="*user*")
    created_at = models.TextField(default="0000-00-00")

    def __str__(self):
        return f"Feedback #{self.id} - {self.created_at}"
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # You can add additional fields like 'status' or 'is_approved' if needed

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
