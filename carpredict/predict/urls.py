# from django.contrib import admin
# from django.urls import path,include
# from predict import views
# urlpatterns = [
#     path("home/", views.home, name='home'),
#     path("",views.registration,name ='registration'),
#     path("login/",views.login,name ='login')
# ]         



from django.contrib import admin
from django.urls import path
from predict import views
urlpatterns = [
  

   
    
    path("",views.SignupPage,name="SignupPage"),
    path("login/",views.LoginPage,name="login"),
    path("home/",views.home,name="home"),
    path("logout/",views.LogoutPage,name="LogoutPage"),
    path("carpriceprediction/",views.carpriceprediction,name="carpriceprediction"),
    


]         