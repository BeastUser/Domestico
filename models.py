from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

dt = models.DateTimeField(default=timezone.now)

# Create your models here.
class Empdetails(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)  # Ensure this is correct
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    work = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()

class contactMe(models.Model):
    cno=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=60)
    email=models.CharField(max_length=30)
    text=models.CharField(max_length=100)
    
    def __str__(self):
        return self.uname

