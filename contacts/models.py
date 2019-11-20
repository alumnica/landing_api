from django.db import models
from django.utils import timezone



# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=16)
    msg = models.TextField()
    creationdate = models.DateTimeField(blank = False, default = timezone.now, null = False)

    def __str__(self):
        return self.name
    
class Suscriber(models.Model):    
    email = models.EmailField(max_length=150)    
    creationdate = models.DateTimeField(blank = False, default = timezone.now, null = False)

    def __str__(self):
        return self.email



