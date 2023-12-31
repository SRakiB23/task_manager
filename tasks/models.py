from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
     PRIORITY_LOW = 'L'
     PRIORITY_MEDIUM = 'M'
     PRIORITY_HIGH = 'H'

     PRIORITY_CHOICES = [
         (PRIORITY_LOW, 'Low'),
         (PRIORITY_MEDIUM, 'Medium'),
         (PRIORITY_HIGH, 'High'),
     ]

     title = models.CharField(max_length=80)
     content = models.CharField(max_length=500)
     date_posted = models.DateTimeField(auto_now_add=True)
     priority = models.CharField(
         max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)
     
     user = models.ForeignKey(User, max_length=10,on_delete=models.CASCADE, null=True)
     
    
# class Review(models.Model):
#      reviewer_name = models.CharField(max_length=100)
#      review_title = models.CharField(max_length= 85)

#      task = models.ForeignKey(Task, on_delete=models.CASCADE)