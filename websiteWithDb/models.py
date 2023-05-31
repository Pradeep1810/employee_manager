from django.db import models

# Create your models here.

class Emploee(models.Model):

    #the columns for the database model

    name = models.CharField(max_length= 20)
    phone_number = models.IntegerField()
    isOnProject = models.BooleanField()
    