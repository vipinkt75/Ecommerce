from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    unique_id=models.CharField(unique=True,max_length=50)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='Product_image')
    description=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name



class Customer(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    


    def __str__(self):
        return self.name
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address =models.TextField()
    city=models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    post=models.IntegerField()
    email=models.CharField(max_length=100)
    additional_info=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    date =models.DateField(auto_now_add=True)


   


    def __str__(self):
        return self.user.username
    

class Order_Item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    image =models.ImageField(upload_to='media/order')
    quantity =models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    payment_id= models.CharField(max_length=100,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    total =models.CharField(max_length=100)

    def __str__(self):
        return self.order.user.username