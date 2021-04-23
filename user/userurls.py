from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('User/Login/',views.userlogin,name="userlogin"),
    path('Salon_Owner/Login/', views.salonlogin, name="salonlogin"),
    path('Salon/Registration/', views.salonregister, name="salonregister"),
    path('User/Registration/', views.userregister, name="userregister"),
    path('Salon/Login/SalonHome', views.salonowner, name="salonowner"),
    path('Salon/Login/SalonHomePage', views.salonhome, name="salonhome"),
    path('Salon/Login/AddSalon', views.addsalon, name="addsalon"),
    path('Salon/Login/UpdateSalon', views.updatesalon, name="updatesalon"),
    path('Logout', views.logouts, name="logouts"),
    ]