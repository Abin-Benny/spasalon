from django.shortcuts import render,redirect
from django.contrib.auth import login,logout

# Create your views here.

def index(request):
    return render(request,"index.html")

def userlogin(request):
    return render(request,"user_login.html")

def salonlogin(request):
    return render(request,"salon_login.html")

def salonregister(request):
    return render(request,"salonregister.html")

def userregister(request):
    return render(request,"userregister.html")

def salonowner(request):
    return render(request, "salonowner.html")

def salonhome(request):
    return render(request, "salonhome.html")

def addsalon(request):
    return render(request,"addsalon.html")

def updatesalon(request):
    return render(request,"updatesalon.html")

def logouts(request):
    logout(request)
    return redirect("salonlogin")