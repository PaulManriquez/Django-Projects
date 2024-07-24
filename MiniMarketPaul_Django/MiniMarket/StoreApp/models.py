from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    Name = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta: #<-- How will appear in the Panel Admin
        verbose_name = 'Category_Product'
        verbose_name_plural = 'Categories_Products'
    
    def __str__(self) -> str:
        return self.Name #<-- every call to the object
                         #gets the name of the category

class Product(models.Model):
    Name = models.CharField(max_length=22)
    Category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='StoreApp',null=True,blank=True)
    Price = models.FloatField()
    Availability = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta: #<-- How will appear in the Panel Admin
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
