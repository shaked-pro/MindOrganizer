from django.db import models
from django.contrib.auth.models import User

# Thought Model 
class Thought(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

