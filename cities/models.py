from django.db import models

class Cities(models.Model):
    
    city = models.CharField(max_length=100,null=True, blank=False)
    city_ascii = models.CharField(max_length=100,null=True, blank=False)
    lat = models.CharField(max_length=100,null=True, blank=False)
    lng = models.CharField(max_length=100,null=True, blank=False)
    country = models.CharField(max_length=100,null=True, blank=False)
    iso2 = models.CharField(max_length=100,null=True, blank=False)
    iso3 = models.CharField(max_length=100,null=True, blank=False)
    admin = models.CharField(max_length=100, null=True, blank=False)
    capital = models.CharField(max_length=100, null=True, blank=False)
    population = models.CharField(max_length=100, null=True, blank=False)
    custom_id = models.CharField(max_length=100, null=True, blank=False)