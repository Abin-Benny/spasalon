from django.db import models

# Create your models here.
class salonlogin(models.Model):
    Username=models.EmailField(max_length=50)
    Password=models.CharField(max_length=20)
   # Role=models.IntegerField(default=1)# 0=admin,1=user

class salonreg(models.Model):
    Login_id=models.ForeignKey(salonlogin,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=20)
    Mobile= models.CharField(max_length=20)
    Address=models.CharField(max_length=250)

class clientlogin(models.Model):
    Username=models.EmailField(max_length=50)
    Password=models.CharField(max_length=20)
   # Role=models.IntegerField(default=1)# 0=admin,1=user

class clientreg(models.Model):
    Login_id=models.ForeignKey(clientlogin,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=20)
    Mobile= models.CharField(max_length=20)
    Address=models.CharField(max_length=250)