
from django.shortcuts import render, redirect
from .forms import RestaurantForm, FoodForm

from .models import *




def addrestaurant(request):
    locations = Restaurant.objects.values('resLocation').distinct()
    title="Add Restaurant"
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success="Data Saved Successfully ..."
                return render(request, 'success.html', {'success':success, 'locations': locations, 'title':title})
            except Exception as e:
                error="Restaurand Id is Already Present !!!"
                return render(request, 'error.html', {'error':error, 'locations': locations, 'title':title})
                
        else:
            error="Data Not Saved !!!!..."
            return render(request, 'error.html', {'error':error, 'locations': locations, 'title':title})
            
    else:
        form = RestaurantForm()
    return render(request, 'AddRestaurant.html', {'form': form, 'locations': locations, 'title':title})



def addfood(request):
    title="Add Food"
    locations = Restaurant.objects.values('resLocation').distinct()
    if request.method == "POST":
        form =FoodForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success="Data Saved Successfully ..."
                return render(request, 'success.html', {'success':success, 'locations': locations, 'title':title})
            except Exception as e:
                error="Food Id is Already Present !!!"
                return render(request, 'error.html', {'error':error, 'locations': locations, 'title':title})
                
        else:
            error="Data Not Saved !!!!..."
            return render(request, 'error.html', {'error':error, 'locations': locations, 'title':title})
            
    else:
        form = FoodForm()
    return render(request, 'AddFood.html', {'form': form, 'locations': locations, 'title':title})




def success(request):
    title="Success"
    locations = Restaurant.objects.values('resLocation').distinct()
    return render(request, 'success.html', {'locations':locations})

def error(request):
    title="Failed"
    locations = Restaurant.objects.values('resLocation').distinct()
    return render(request, 'error.html', {'locations':locations})


def displayres(request):
    title="Restaurant List"
    locations = Restaurant.objects.values('resLocation').distinct()
    
    resdata=Restaurant.objects.all()
    
    col1="Restaurant Id"
    col2="Restaurant Name"
    col3="Restaurant Location"
    
    return render(request, 'display.html', {'locations':locations,'resdata':resdata, 'col1':col1, 'col2':col2, 'col3':col3, 'title':title})


def displayfood(request):
    title="Food List"
    locations = Restaurant.objects.values('resLocation').distinct()
    
    fooddata=Food.objects.select_related('restaurant').all()
    print(fooddata)
    
    col1="Restaurant Name"
    col2="Food Id"
    col3="Food Name"
    col4="Food Price"
    
    return render(request, 'display.html', {
        'locations':locations,
        'fooddata':fooddata,
        'col1':col1,
        'col2':col2,
        'col3':col3,
        'col4':col4,
        'title':title})

def display(request):
    title="Home"
    locations = Restaurant.objects.values('resLocation').distinct()
    return render(request, 'display.html', {'locations':locations, 'title':title})


def search(request):
    title="Search"
    locations = Restaurant.objects.values('resLocation').distinct()
    inpdata=request.POST.get('searchinp')
    select=request.POST.get('option')
    selectloc=request.POST.get('loclist')

    
    if select =="None" and inpdata:
        error="Select Valid Option !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
    
    if (select and not inpdata) and (select  and not selectloc):
        error="Enter Valid Data !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
    
    if  (select  and selectloc=="None") and (not inpdata):
        error="Please Select the location !!!"
        return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
    
    if select=="foodId" and inpdata:
        title="Search by Food Id"
        fooddata=Food.objects.select_related('restaurant').filter(foodId__iexact=inpdata)
        print(fooddata)
        
        col1="Restaurant Name"
        col2="Food Id"
        col3="Food Name"
        col4="Food Price"
        
        return render(request, 'display.html', {'locations':locations, 'fooddata':fooddata, 'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'title':title})
            
    if select=="resId" and inpdata:
        title="Search by Restaurant Id"
        resdata=Restaurant.objects.filter(resId__iexact=inpdata)
        col1="Restaurant Id"
        col2="Restaurant Name"
        col3="Restaurant Location"

        return render(request, 'display.html', {'locations':locations, 'resdata':resdata, 'col1':col1, 'col2':col2, 'col3':col3, 'title':title})
            
    if select == "location" and selectloc:
        title="Search by Location"
        resdata = Restaurant.objects.filter(resLocation=selectloc)
        col1, col2, col3 = "Restaurant Id", "Restaurant Name", "Restaurant Location"
        return render(request, 'display.html', {'locations': locations, 'resdata': resdata, 'col1': col1, 'col2': col2, 'col3': col3, 'title':title})
    
    else:
        error="Enter Valid Data to search !!!"
        return render(request, 'display.html', {'locations':locations,'error':error, 'title':title})
        


def delete(request):
    title="Delete Page"
    locations = Restaurant.objects.values('resLocation').distinct()
    
    error="Data not Available !!!"
    success="Deleted Successfully .."
    
    option=request.POST.get('option')
    if option=="None":
        error="Select the option first !!!!"
        return render(request, "error.html", {'error':error, 'locations':locations, 'title':title})
    inpdata=request.POST.get('inp') 
    
    print(option, inpdata)
    
    if option=="foodId":
        
        if not inpdata:
            error="Enter the valid foodid to delete !!!"
            return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
        
        if option and inpdata:
            fooddata=Food.objects.filter(foodId__iexact=inpdata)
            print(fooddata)
            if fooddata.exists():
                fooddata.delete()
                success="Data Deleted Successfully ...."
                return render(request, 'success.html', {'success':success, 'locations':locations, 'title':title})
            else:
                error="Data does not available in the database !!!"
                return render(request, 'error.html', {'error':error, 'locations':locations, 'title':title})
        
    elif option=="resId":
    
        if option and not inpdata:
            error="Enter the valid food id to delete !!!"
            return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
        
        if inpdata and option=="None":
            error="Select valid option to delete !!!"
            return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
        
        if not inpdata and option=="None":
            error="Enter valid data to delete"
            return render(request, 'display.html', {'error':error, 'locations':locations, 'title':title})
        
        if option and inpdata:
            resdata=Restaurant.objects.filter(resId__iexact=inpdata).get()
            print(resdata)
            if resdata:
                resdata.delete()
                success="Data Deleted Successfully ...."
                return render(request, 'success.html', {'success':success, 'locations':locations, 'title':title})
            else:
                error="Data does not available in the database !!!"
                return render(request, 'error.html', {'error':error, 'locations':locations, 'title':title})
            
  
    return render(request, 'delete.html', {'locations':locations, 'title':title})







def update(request):
    title="Update"
    locations = Restaurant.objects.values('resLocation').distinct()
    
    return render(request, 'update.html', {'locations':locations, 'title':title})

def updatefood(request):
    title="Update Food"
    locations = Restaurant.objects.values('resLocation').distinct()
    
    fId = request.POST.get('foodid')
    fName= request.POST.get('foodname')
    fPrice = request.POST.get('foodprice')

    foodata=Food.objects.filter(foodId__iexact=fId).get()
    
    if foodata:
        if fName:
            foodata.foodName=fName
            print(foodata.foodName)
        
        if fPrice:
            foodata.foodPrice=fPrice
            print(foodata.foodPrice)
        
        foodata.save()
        success="Data Updated Successfully...."
        return render(request, 'success.html', {'success':success, 'locations':locations, 'title':title})
    
    else:
        error="Food Not available with this id !!!"
        return render(request, 'error.html', {'error':error, 'locations':locations, 'title':title})
    
    
        
def updaterest(request):
    title="Update Restaurant"
    locations = Restaurant.objects.values('resLocation').distinct()
    rId = request.POST.get('resid')
    rName= request.POST.get('resname')
    rloc = request.POST.get('resprice')
    
    resdata = Restaurant.objects.filter(resId__iexact=rId).get()
    
    if resdata:
        if rName:
            resdata.resName=rName
        
        if rloc:
            resdata.resLocation=rloc
            
        resdata.save()
        success="Data Updated Successfully...."
        return render(request, 'success.html', {'success':success, 'locations':locations, 'title':title})
    
    else:
        error="Food Not available with this id !!!"
        return render(request, 'error.html', {'error':error, 'locations':locations, 'title':title})
    
    



