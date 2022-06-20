from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class User(models.Model):
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     birthday = models.DateField()
#     username = models.CharField(max_length=100)
#     email = models.EmailField(min_length= 6,max_length=70)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name