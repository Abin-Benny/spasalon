from django.db import models

# Create your models here.
class salonlogin(models.Model):
    Username=models.EmailField(max_length=50)
    Password=models.CharField(max_length=250)


class salonreg(models.Model):
    Login_id=models.ForeignKey(salonlogin,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=250)
    Mobile= models.CharField(max_length=20)
    Address=models.CharField(max_length=250)

class clientlogin(models.Model):
    Username=models.EmailField(max_length=50)
    Password=models.CharField(max_length=250)
   # Role=models.IntegerField(default=1)# 0=admin,1=user

class clientreg(models.Model):
    Login_id=models.ForeignKey(clientlogin,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=250)
    Mobile= models.CharField(max_length=20)
    Address=models.CharField(max_length=250)

class salondetails(models.Model):
    Login_id =models.ForeignKey(salonlogin,on_delete=models.CASCADE)
    Salon_name=models.CharField(max_length=50)
    Opening_hours=models.CharField(max_length=50)
    Services=models.CharField(max_length=300)
    Service_price=models.CharField(max_length=350)
    Image = models.ImageField(upload_to='images')
    Address=models.CharField(max_length=250)

class bookingdetails(models.Model):
    Lid = models.CharField(max_length=50)
    Slid = models.CharField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Mobile = models.CharField(max_length=20)
    Services = models.CharField(max_length=40)
    Date = models.CharField(max_length=50)
    Time = models.TimeField()
    Status = models.CharField(max_length=20)

class reviews(models.Model):
    Uid = models.CharField(max_length=50)
    Sid = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Review = models.CharField(max_length=250)


class contact(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=50)

    def __str__(self):
        return self.Subject
