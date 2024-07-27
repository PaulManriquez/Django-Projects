from django.db import models
from django.contrib.auth import get_user_model
from StoreApp.models import Product
from django.db.models import F,Sum,FloatField
# Create your models here.
User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.id
    
    #The @property decorator in Python allows a method to be accessed like an attribute. 
    #This means you can call order.Total instead of order.Total().
    @property
    def Total(self):
        return self.orderline_set.aggregate(
            total=Sum(F('product_id__Price') * F('quantity'), output_field=FloatField())
        )['total']

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']

class OrderLine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)  
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.quantity} units of {self.product_id.Name}'

    class Meta:
        db_table = 'Order_Line'
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'
        ordering = ['id']

