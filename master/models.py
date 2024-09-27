
from django.db import models

class Item(models.Model):
    
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)  
    image=models.ImageField(upload_to='item_images', blank=True,null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Supplier(models.Model):
    
    supplier_name=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=15)
    address=models.CharField(max_length=400)
    status = models.BooleanField(default=True) 
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.supplier_name
    
    