from django.db import models

class student(models.Model):

    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True, blank=True)
    file=models.FileField()

class cars(models.Model):
    car_name = models.CharField(max_length=100)
    speed=models.IntegerField(default=60)
    
    def __str__(self):
        return self.car_name
    