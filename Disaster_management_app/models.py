from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CERT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    responsibilities = models.TextField()

class EmergencyPlan(models.Model):
    community = models.OneToOneField('Community', on_delete=models.CASCADE)
    plan_text = models.TextField()

class Resource(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='DefaultLocation')
    # location = models.CharField(max_length=255)
    description = models.TextField()

class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    

