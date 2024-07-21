from django.db import models

from datetime import date
# Create your models here.

class Customer(models.Model):
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Email = models.EmailField(blank=True,null=True)#<--Make optional this field 
    Phone = models.CharField(max_length=12)
    #Add a description 
    def __str__(self) -> str:
        return f'Customer Table\n Name:{self.Name} Address:{self.Address} Email:{self.Email} Phone:{self.Phone}'


class Items(models.Model):
    Name = models.CharField(max_length=30)
    Section = models.CharField(max_length=20, verbose_name='Section(Clasify)')#Change the name how will appear in the field name 
    Price = models.FloatField()
    def __str__(self) -> str:
        return f'Items Table\n Name:{self.Name} Section:{self.Section} Price:{self.Price}'



class Orders(models.Model):
    Order_Number = models.CharField(max_length=30)
    Name_Item = models.CharField(max_length=30,default='Default Item')
    Section = models.CharField(max_length=20)
    Price = models.FloatField()
    Order_Date = models.DateField(default=date.today)
    def __str__(self) -> str:
        return f'Orders Table\n Order_Number:{self.Order_Number} Section:{self.Section} Price:{self.Price}'



