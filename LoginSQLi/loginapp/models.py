from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def authenticate_user(self, input_username, input_password):
        query = f"SELECT * FROM User WHERE username = '{input_username}' AND password = '{input_password}'"
        result = User.objects.raw(query)
        return result
