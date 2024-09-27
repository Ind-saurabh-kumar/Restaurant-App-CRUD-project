from django import forms
from .models import Restaurant, Food

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['resId', 'resName', 'resLocation']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['restaurant', 'foodId', 'foodName', 'foodPrice']
