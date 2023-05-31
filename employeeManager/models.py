from django.db import models

# Create your models here.

#our emp model here

class Employee(models.Model):

    name = models.CharField(max_length= 20)

    phone_number = models.CharField(max_length= 10)

    address = models.TextField()

    isOnTable = models.BooleanField(default=False)

    age = models.IntegerField()

    def __str__(self):

        return self.name

        #this is a str method that we are overridding 

#creating a employee review model

class EmpReview(models.Model):

    name = models.CharField(max_length = 20 , default= 'Anonymous')

    pics = models.ImageField(upload_to = "profile/" , null=True)

    rating = models.IntegerField(default=0)

    department = models.CharField(max_length=20 , default = 'Company Name')


    

    
