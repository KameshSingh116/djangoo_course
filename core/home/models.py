from django.db import models

class student(models.Model):

    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True, blank=True)
    file=models.FileField()