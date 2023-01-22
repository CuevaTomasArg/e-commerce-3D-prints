from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return f'{self.name}'


class Filament(models.Model):
    name = models.CharField(max_length=75, blank=True,null=True)
    brad = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product_image')
    description = models.CharField(max_length=256, blank= True, null=True)
    stock = models.IntegerField(blank= True, null=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self) :
        return f'{self.name} - {self.category} - {self.price}'
    


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product_image')
    description = models.CharField(max_length=256, blank= True, null=True)
    stock = models.IntegerField(blank= True, null=True, default=1)
    in_cart = models.BooleanField(default=False)
    def __str__(self) :
        return f'{self.name} - {self.category} - {self.price}'



class Commentary(models.Model):
    commentary = models.CharField(max_length=256)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) :
        return f'{self.commentary} - {self.user.email}'

    
class Query(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    query = models.CharField(max_length=256)

    
class Customizable(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='customizable_image')
    description = models.CharField(max_length=256, null=True, blank=True)
    amount = models.IntegerField(blank = True, null=True, default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    


class Bought(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    direction = models.CharField(max_length = 256)
    direction_number = models.IntegerField()
    references = models.CharField(max_length=256, blank= True, null = True)
    cp = models.IntegerField()
    date = models.DateTimeField()
    phone = models.CharField(max_length=19,blank=True, null = True)
    receipt = models.ImageField(upload_to= "receipt", default = None)
    quantity_of_products = models.IntegerField(null=True,blank=True)
    accumulated = models.IntegerField(null=True,blank=True)
    customizable = models.BooleanField(default=False)
    


class ProductBougth(models.Model):
    Bought = models.ForeignKey(Bought, on_delete = models.CASCADE, null = True, blank= True)
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank = True, null=True, default=1)
    accumulated = models.IntegerField(blank=True, null=True)


class Province(models.Model):
    name = models.CharField(max_length=32)
    shipping_price = models.IntegerField()
    def __str__(self):
        return f'{self.name} - {self.shipping_price}'
    