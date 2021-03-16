from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField(default=30)
    image=models.ImageField(upload_to='images/realtor',default=None)

    def __str__(self):
        return self.Name
class Housing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE)
    House_Title=models.CharField(max_length=50)
    House_Address=models.CharField(max_length=500)
    house_Desc=models.CharField(max_length=1000)
    Price=models.FloatField(default=0)
    House_Area=models.IntegerField(default=0)
    No_of_rooms=models.IntegerField(default=0)
    Garrage=models.BooleanField(default=False)
    Main_Photo=models.ImageField(upload_to='images/home',default=None)
    Inside_Photo=models.ImageField(upload_to='images/home',default=None)
    publish_date=models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.House_Title











