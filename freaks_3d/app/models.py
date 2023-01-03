from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=75)
    mark = models.CharField(max_length=75,null=True,blank=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product_image')
    description = models.CharField(max_length=256, blank= True, null=True)
    stock = models.IntegerField(blank= True, null=True)
    amount = models.IntegerField(blank = True, null=True, default=1)
    
    def __str__(self) :
        return f'{self.name} - {self.category} - {self.price}'

class Commentary(models.Model):
    commentary = models.CharField(max_length=256)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
class Query(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    query = models.CharField(max_length=256)
    
class Customizable(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='customizable_image')
    description = models.CharField(max_length=256, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

class Bought(models.Model):
    user = models.Foreingkey(User, on_delete = models.CASCADE, null = True, blanck = True)
    direction = models.CharField(max_length = 256)
    cp = models.CharField(max_length = 32)
    date = models.DateTimeField()