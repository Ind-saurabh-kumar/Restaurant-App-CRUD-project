from django import forms

from django.db import models

# Create your models here.

class Restaurant(models.Model):
    resId = models.CharField(max_length=20, primary_key=True)
    resName = models.CharField(max_length=50)
    resLocation=models.CharField(max_length=50)

    def __str__(self):
        return f"Id: {self.resId} ----- Name: {self.resName} ----- Location: {self.resLocation}"



class Food(models.Model):
    restaurant =models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    foodId = models.CharField(max_length=20, primary_key=True)
    foodName = models.CharField(max_length=50)
    foodPrice = models.IntegerField()
    
    
    def __str__(self):
        return f" RestaurantId: {self.restaurant.resId} -----> FoodId: {self.foodId} ----- Name: {self.foodName} ----- Price: {self.foodPrice}"
    
    

    
    
