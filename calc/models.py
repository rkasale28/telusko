from django.db import models

# Create your models here.
class Destination:
    id : int
    name : str
    dest : str
    price : int

    def __init__(self, a, b,c,d): 
        self.id = a 
        self.name = b
        self.dest=c
        self.price=d 