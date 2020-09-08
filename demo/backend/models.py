from django.db import models
# from django.core.exceptions import DoesNotExist

# Create your models here.
class Township(models.Model):
  name=models.CharField(max_length=200)
  objects=models.Manager()
  def __str__(self):
    return self.name
class Restaurant(models.Model):
  township=models.ForeignKey(Township,on_delete=models.CASCADE)
  name=models.CharField(max_length=200)
  objects=models.Manager()
  def __str__(self):
    return self.name
  
class Menu(models.Model):
  restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
  name=models.CharField(max_length=200)
  price=models.CharField(max_length=200)
  objects=models.Manager()