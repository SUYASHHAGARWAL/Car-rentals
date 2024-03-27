from django.db import models

# Create your models here.
class category(models.Model):
    categoryname = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=150, blank=False, default='')
    # icon = models.ImageField(upload_to='static/')

class subcategory(models.Model):
    categoryid = models.CharField(max_length=70, blank=False, default='')
    companyname = models.CharField(max_length=70, blank=False, default='')
    subcategoryname=models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=150, blank=False, default='')
    # icon = models.ImageField(upload_to='static/')

class Vehicle(models.Model):
    agencyid=models.CharField(max_length=70, blank=False, default='')
    categoryid=models.CharField(max_length=70, blank=False, default='')
    subcategoryid=models.CharField(max_length=70, blank=False, default='')
    modelyear=models.CharField(max_length=70, blank=False, default='')
    variant=models.CharField(max_length=70, blank=False, default='')
    price=models.CharField(max_length=70, blank=False, default='')
    insured=models.CharField(max_length=70, blank=False, default='')
    registrationno=models.CharField(max_length=70, blank=False, default='')
    ownername=models.CharField(max_length=70, blank=False, default='')
    mobileno=models.CharField(max_length=70, blank=False, default='')
    colour=models.CharField(max_length=70, blank=False, default='')
    fueltype=models.CharField(max_length=70, blank=False, default='')
    no_of_seats=models.CharField(max_length=70, blank=False, default='')
    transmissiontype=models.CharField(max_length=70, blank=False, default='')
    picture = models.ImageField(upload_to='static/')
    city = models.CharField(max_length=150, blank=False, default='')
    picture2 = models.ImageField(upload_to='static/')
    picture3 = models.ImageField(upload_to='static/')
    picture4 = models.ImageField(upload_to='static/')
    picture5 = models.ImageField(upload_to='static/')

class Administrator(models.Model):
    adminname = models.CharField(max_length=70, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    emailid= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')

class Agencies(models.Model):
    Agencyname = models.CharField(max_length=70, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    emailid= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    city = models.CharField(max_length=150, blank=False, default='')

class User(models.Model):
    Username = models.CharField(max_length=70, blank=False, default='')
    UserEmail = models.CharField(max_length=70, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    AadharNumber= models.CharField(max_length=15, blank=False, default='')
    licenceNumber= models.CharField(max_length=15, blank=False, default='')

class Drivers(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    AadharNumber= models.CharField(max_length=15, blank=False, default='')
    licenceNumber= models.CharField(max_length=15, blank=False, default='')
    appointed_to_someone = models.CharField(max_length=15, blank=False, default='')
    
