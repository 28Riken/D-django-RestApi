from django.db import models

# Create your models here.

class Employee(models.Model):
    eId = models.IntegerField()
    eFirstName = models.CharField(max_length=50)
    eSal = models.FloatField()


    def __str__(self):
        return f"{self.eId}--{self.eFirstName}"
         
