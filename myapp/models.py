from django.db import models

# Create your models here.

class Netflix(models.Model):
   title= models.CharField(max_length=100)
   genre= models.CharField(max_length=100)
   premiere= models.CharField(max_length=100)
   runtime= models.CharField(max_length=100)
   imbb_score= models.CharField(max_length=100)
   language= models.CharField(max_length=100)

   def __str__(self):
    return self.title



    