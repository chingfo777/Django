from django.db import models

# Create your models here.
# Creating Company Model
# class Company(models.Model):
#     company_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     about = models.TextField()
#     type = models.CharField(max_length=100, choices=(
#         ('IT','IT'),
#         ('Non IT','Non IT'),
#         ("Mobiles Phones", "Mobile Phones")
#     ))
#     added_date = models.DateTimeField(auto_now = True)
#     active = models.BooleanField(default=True)

# Employee Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    # company =models.ForeignKey(Company,on_delete = models.CASCADE)
