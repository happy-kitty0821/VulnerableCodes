from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def authenticate_user(self, input_username, input_password):
        query = f"SELECT * FROM User WHERE username = '{input_username}' AND password = '{input_password}'"
        result = User.objects.raw(query)
        return result


class Feedbacks(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    contact = models.CharField(max_length=15)
    message = models.CharField(max_length=1000) 
    
    def __str__(self):
        return f"{self.username} {self.email} {self.contact} {self.message}"