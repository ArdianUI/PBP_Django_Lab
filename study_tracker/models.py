from django.db import models

# Create your models here.

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50)
    progress = models.IntegerField()
    description = models.TextField()
