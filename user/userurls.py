from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('User/Login/',views.userlogin,name="userlogin"),
    path('Salon_Owner/Login/', views.salonlogins, name="salonlogin"),
    path('Salon/Registration/', views.salonregister, name="salonregister"),
    path('User/Registration/', views.userregister, name="userregister"),
    path('Salon/Login/SalonHome', views.salonowner, name="salonowner"),
    path('Salon/Login/SalonHomePage', views.salonhome, name="salonhome"),
    path('Salon/Login/AddSalon', views.addsalon, name="addsalon"),
    path('Salon/Login/UpdateSalon', views.updatesalon, name="updatesalon"),
    path('Salon/Login/Bookings', views.bookings, name="bookings"),
    path('Salon/Login/Bookings/UpdateStatus/<ids>', views.statusupdate, name="statusupdate"),
    path('User/Login/UserHomePage', views.userhome, name="userhome"),
    path('User/Login/HomePage', views.userhomepay, name="userhomepay"),
    path('User/Login/SalonAppointment/<id>', views.booking, name="booking"),
    path('User/Login/SalonAppointmentSubmit/<id>', views.appsubmit, name="appsubmit"),
    path('User/Login/Appointment/Payment/', views.payment, name="payment"),
    path('User/Login/Appointment/BankPayment/', views.pay, name="pay"),
    path('Logout', views.logouts, name="logouts"),
    ]