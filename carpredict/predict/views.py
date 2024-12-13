from django.shortcuts import render,HttpResponse,redirect
from predict.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import joblib
import pandas as pd
import numpy as np
import sklearn as sns

import joblib
import os
from django.conf import settings
from django.http import JsonResponse 



model=None
model_path = os.path.join(settings.BASE_DIR, 'car_price_prediction.pkl')
with open(model_path, 'rb') as file:
    model = joblib.load(file)

COLUMNS = [
    'year', 
    'brand', 
    'model_name', 
    'distance_travelled(kms)', 
    'fuel_type',
    'city'
]

def carpriceprediction(request):
    if request.method == 'POST':
        input_features = pd.DataFrame(np.zeros((1,6)), columns=COLUMNS)
        
        # Extracting the input features from the form
        data = request.POST

        input_features['year'] = float(request.POST.get('year', 0))
        input_features['brand'] = request.POST.get('company', '')
        input_features['model_name'] = request.POST.get('model', '')
        input_features['distance_travelled(kms)'] = float(request.POST.get('km', 0))
        input_features['fuel_type'] = request.POST.get('fuel', '')
        input_features['city'] = request.POST.get('city', '')

        print(input_features)

        try:
            # Predict the price using the model
            predicted_price = model.predict(input_features)
            print("Predicted Price: ", int(predicted_price))

            # Return JSON response with predicted price
            return JsonResponse({'predicted_price': int(predicted_price)})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, "car_price_prediction.html")



def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        useremail=request.POST['useremail']
        message=request.POST['message']
        print(username,useremail,message)
        contact=Contact.objects.create(name=username,email=useremail,msg=message)
        contact.save()
    return render(request,"home.html") 



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Passwords do not match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')
        return HttpResponse("Your password and confrom password are not Same!!")
    return render(request,"signup.html")


        
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


