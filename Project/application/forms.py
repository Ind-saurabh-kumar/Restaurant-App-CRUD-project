from django import forms
from .models import Restaurant, Food
from django.core.exceptions import ValidationError

class RestaurantForm(forms.ModelForm):
    resId = forms.IntegerField(label='Food ID')
    class Meta:
        model = Restaurant
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.resName = instance.resName.title()
        instance.resLocation = instance.resLocation.title()

        # Check for existing record by unique identifier, e.g., resId
        instance.resId="R"+str(instance.resId)
        if Restaurant.objects.filter(resId__iexact=instance.resId).exists():
            raise ValidationError("A restaurant with this ID already exists.")

        if commit:
            instance.save()
        return instance

class FoodForm(forms.ModelForm):
    foodId = forms.IntegerField(label='Food ID')
    class Meta:
        model = Food
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.foodName = instance.foodName.title()

        # Ensure the restaurant foreign key is set before using it
        if instance.restaurant:  # Check if the foreign key is set
            # Construct foodId by concatenating restaurant resId and current foodId
            foodId = "F"+str(instance.foodId)  # Save the original foodId
            instance.foodId = f"{instance.restaurant.resId}{foodId}"  # Combine restaurant ID and food ID

        # Check for existing record by unique identifier
        if Food.objects.filter(foodId__iexact=instance.foodId).exists():
            raise ValidationError("A food item with this ID already exists.")

        if commit:
            instance.save()
        return instance