from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(default=20)
    mobilenumber = models.CharField(max_length=10,null=True)
    uimg = models.ImageField(upload_to='Profilepics/', default = 'logo.png')
    t = [(1,'Guest'),(2,'Manager'),(3,'User')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Manager'),(3,'User')]
    rltype = models.IntegerField(choices=f)
    is_checked = models.BooleanField(default=False)
    Uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Itemlist(models.Model):
    y=[('Indian','Indian'),('Imported', 'Imported'),('Select item-type', 'Select item-type')] 
    iname=models.CharField(max_length=50)
    icategory=models.CharField(choices=y,default="Select item-type",max_length=50)
    iprice=models.DecimalField(decimal_places=3,max_digits=10)
    iimage=models.ImageField(upload_to='Itemimages/',default='logo.png')

    def __str__(self):
        return self.iname

class Userorder(models.Model):
    iname = models.ForeignKey(Itemlist,on_delete=models.CASCADE)
    iname_quantity = models.IntegerField(default=0)
    contactnumber = models.CharField(max_length=10,null=True)
    Address = models.CharField(max_length=5000,null=True)
    person = models.CharField(max_length=50,default="Type your name")
