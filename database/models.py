from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=100,null=True)
    user_type=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user_type

class Customer(models.Model):
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)

class Address(models.Model):
    room=models.CharField(max_length=100,blank=False)
    building=models.CharField(max_length=100,blank=False)
    road=models.CharField(max_length=100,blank=False)
    area=models.CharField(max_length=100,blank=False)
    city=models.CharField(max_length=100,blank=False)
    pincode=models.CharField(max_length=100,blank=False)
    landmark=models.CharField(max_length=100,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ORDER_STATUS_CHOICES=[
        ('D','Delivered'),
        ('S','Shipped'),
        ('P','Placed')
    ]
    status=models.CharField(max_length=1,choices=ORDER_STATUS_CHOICES,default='P')

class ItemInOrder(models.Model):
    name=models.CharField(max_length=100,null=True) 
    price=models.IntegerField(null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Item(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='pics')

class Publication(models.Model):
    title = models.CharField(max_length=30)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

class Student(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    ORDER_STATUS_CHOICES=[
        ('D','Delivered'),
        ('S','Shipped'),
        ('P','Placed')
    ]
    status=models.CharField(max_length=1,choices=ORDER_STATUS_CHOICES,default='P')
