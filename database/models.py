from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email_id=models.EmailField(null=True)
    user_name=models.CharField(max_length=100,null=True)
    pwd=models.CharField(max_length=100,null=True)
    user_type=models.CharField(max_length=100,null=True)
