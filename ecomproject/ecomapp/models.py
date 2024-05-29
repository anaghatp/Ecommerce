from django.db import models


from django.db import models
from django.contrib.auth.models import User,auth

class Item(models.Model):
    itemname = models.CharField(max_length=100)

class Product(models.Model):
    catname = models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    proname = models.CharField(max_length=100)
    proprice = models.IntegerField(null=True)
    prodes = models.CharField(max_length=250)
    proimage = models.ImageField(null=True,upload_to="image/")
    
class userr(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    useraddress = models.CharField(max_length=250)
    usernumber = models.IntegerField()
    userimage = models.ImageField(null=True,upload_to="image/")
    
    
class Cart(models.Model):
    ucart = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    uproduct = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.quantity * self.uproduct.proprice  
