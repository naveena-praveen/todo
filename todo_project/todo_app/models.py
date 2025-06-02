from django.db import models


class task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    priority=models.CharField(max_length=100,default="low")
    
    