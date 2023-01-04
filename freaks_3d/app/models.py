from django.db import models
# from django.contrib.auth.models import User

class UserFreaks3D(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=19)
    name = models.CharField(max_length=75)

class Category(models.Model):
    name = models.CharField(max_length=75)
    brand = models.CharField(max_length=75,null=True,blank=True)

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
    user = models.ForeignKey(UserFreaks3D,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) :
        return f'{self.commentary} - {self.user.email}'

    
class Query(models.Model):
    user = models.ForeignKey(UserFreaks3D,on_delete=models.CASCADE,null=True,blank=True)
    query = models.CharField(max_length=256)

    
class Customizable(models.Model):
    user = models.ForeignKey(UserFreaks3D,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='customizable_image')
    description = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=19,null=True, blank=True)


class Bought(models.Model):
    user = models.ForeignKey(UserFreaks3D,on_delete=models.CASCADE)
    direction = models.CharField(max_length = 256)
    direction_number = models.IntegerField()
    cp = models.IntegerField()
    date = models.DateTimeField()


class ProductBougth(models.Model):
    Bought = models.ForeignKey(Bought, on_delete = models.CASCADE, null = True, blank= True)
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    amount = models.IntegerField(blank = True, null=True, default=1)
    accumulated = models.IntegerField()
    