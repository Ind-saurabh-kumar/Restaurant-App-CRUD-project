
from django.shortcuts import render, redirect
from .forms import RestaurantForm, FoodForm

from .models import *


locations = Restaurant.objects.values('resLocation').distinct()

def addrestaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = RestaurantForm()
    return render(request, 'AddRestaurant.html', {'form': form, 'locations':locations})


def addfood(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = FoodForm()
    return render(request, 'AddFood.html', {'form': form, 'locations':locations})


def success(request):
    return render(request, 'success.html')


def displayres(request):
    
    resdata=Restaurant.objects.all()
    
    col1="Restaurant Id"
    col2="Restaurant Name"
    col3="Restaurant Location"
    
    return render(request, 'display.html', {'locations':locations,'resdata':resdata, 'col1':col1, 'col2':col2, 'col3':col3})


def displayfood(request):
    
    fooddata=Food.objects.select_related('restaurant').all()
    print(fooddata)
    
    col1="Restaurant Name"
    col2="Food Id"
    col3="Food Name"
    col4="Food Price"
    
    return render(request, 'display.html', {'locations':locations,'fooddata':fooddata, 'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4})

def display(request):
    
    locations = Restaurant.objects.values('resLocation').distinct()
    return render(request, 'display.html', {'locations':locations})


def search(request):
    inpdata=request.POST.get('searchinp')
    select=request.POST.get('option')
    selectloc=request.POST.get('loclist')
    
    print(select)
    print(selectloc)
    
    if select =="None" and inpdata:
        error="Select Valid Option !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations})
    
    if (select and not inpdata) and (select  and not selectloc):
        error="Enter Valid Data !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations})
    
    if  (select  and selectloc=="None") and (not inpdata):
        error="Please Select the location !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations})
    
    if select=="foodId" and inpdata:
        fooddata=Food.objects.select_related('restaurant').filter(foodId__iexact=inpdata)
        print(fooddata)
        
        col1="Restaurant Name"
        col2="Food Id"
        col3="Food Name"
        col4="Food Price"
        
        return render(request, 'display.html', {'locations':locations, 'fooddata':fooddata, 'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4})
            
    if select=="resId" and inpdata:
        resdata=Restaurant.objects.filter(resId__iexact=inpdata)
        col1="Restaurant Id"
        col2="Restaurant Name"
        col3="Restaurant Location"

        return render(request, 'display.html', {'locations':locations, 'resdata':resdata, 'col1':col1, 'col2':col2, 'col3':col3})
            
    if select == "location" and selectloc:
        resdata = Restaurant.objects.filter(resLocation=selectloc)
        col1, col2, col3 = "Restaurant Id", "Restaurant Name", "Restaurant Location"
        return render(request, 'display.html', {'locations': locations, 'resdata': resdata, 'col1': col1, 'col2': col2, 'col3': col3})
    
    else:
        error="Enter Valid Data to search !!!"
        return render(request, 'display.html', {'locations':locations,'error':error})
        


def delete(request):
    
    error="Data not Available !!!"
    success="Deleted Successfully .."
    
    option=request.POST.get('option')
    inpdata=request.POST.get('inp') 
    
    print(option, inpdata)
    
    if option=="foodId":
        
        if option and not inpdata:
            error="Enter the valid foodid to delete !!!"
            return render(request, 'display.html', {'error':error})
        
        if inpdata and not option:
            error="Select valid option to delete !!!"
            return render(request, 'display.html', {'error':error})
        
        if not inpdata and not option:
            error="Enter valid data to delete"
            return render(request, 'display.html', {'error':error})
        
        if option and inpdata:
            fooddata=Food.objects.filter(foodId__iexact=inpdata).get()
            print(fooddata)
            if fooddata:
                fooddata.delete()
                success="Data Deleted Successfully ...."
                return render(request, 'delete.html', {'success':success})
            else:
                error="Data does not available in the database !!!"
                return render(request, 'delete.html', {'error':error})
        
    elif option=="resId":
    
        if option and not inpdata:
            error="Enter the valid foodid to delete !!!"
            return render(request, 'display.html', {'error':error})
        
        if inpdata and not option:
            error="Select valid option to delete !!!"
            return render(request, 'display.html', {'error':error})
        
        if not inpdata and not option:
            error="Enter valid data to delete"
            return render(request, 'display.html', {'error':error})
        
        if option and inpdata:
            resdata=Restaurant.objects.filter(resId__iexact=inpdata).get()
            print(resdata)
            if resdata:
                resdata.delete()
                success="Data Deleted Successfully ...."
                return render(request, 'delete.html', {'success':success})
            else:
                error="Data does not available in the database !!!"
                return render(request, 'delete.html', {'error':error})
            
  
    return render(request, 'delete.html')



def updatefood(request):
    
    
    return render(request, 'update.html') 



def updaterest(request):
    return render(request, 'update.html')



