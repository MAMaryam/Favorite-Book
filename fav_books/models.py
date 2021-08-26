from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, post_date):
        errors = {}

        if(len(post_date['first_name']) < 4):
            errors['first_name'] = "first_name must be at least 4 characters"

        return errors 

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Books(models.Model):
    Title = models.CharField(max_length=255)
    Discription = models.CharField(max_length= 500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
