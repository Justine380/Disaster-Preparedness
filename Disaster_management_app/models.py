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
    
    

class EnvironmentalFactors(models.Model):
    temperature = models.FloatField(default=0.0, blank=True, null=True)
    humidity = models.FloatField(default=0.0 , blank=True, null=True)
    dewpoint = models.FloatField(default=0.0 , blank=True, null=True)
    land_surface_temperature = models.FloatField(default=0.0 , blank=True, null=True)
    low_atmospheric_pressure = models.FloatField(default=0.0 , blank=True, null=True)
    streamflow_river_discharge = models.FloatField(default=0.0 , blank=True, null=True)
    unhealthy_vegetation = models.FloatField(default=0.0 , blank=True, null=True)
    smoking_indoors = models.FloatField(default=0.0 , blank=True, null=True)
    smoke_detectors = models.FloatField(default=0.0 , blank=True, null=True)
    fire_extinguishers = models.FloatField(default=0.0 , blank=True, null=True)
    open_flame = models.FloatField(default=0.0 , blank=True, null=True)
    high_transmission_rate = models.FloatField(default=0.0  , blank=True, null=True)
    high_hospitalized_rate = models.FloatField(default=0.0 , blank=True, null=True)
    high_number_of_cases = models.FloatField(default=0.0 , blank=True, null=True)

    def __str__(self):
        return f"Environmental Factors: {self.id}"

