from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('Salon/',views.salon,name="salon"),
    path('User/Login/',views.userlogin,name="userlogin"),
    path('Salon_Owner/Login/', views.salonlogins, name="salonlogin"),
    path('Salon/Registration/', views.salonregister, name="salonregister"),
    path('User/Registration/', views.userregister, name="userregister"),
    path('Salon/Login/SalonHome', views.salonowner, name="salonowner"),
    path('Salon/Login/SalonHomePage', views.salonhome, name="salonhome"),
    path('Salon/Login/AddSalon', views.addsalon, name="addsalon"),
    path('Salon/Login/UpdateSalon', views.updatesalon, name="updatesalon"),
    path('Salon/Login/Bookings', views.bookings, name="bookings"),
    path('Salon/Login/Appointments', views.salonappointments, name="salonappointments"),
    path('Salon/Login/TodayAppointments', views.todayappointments, name="todayappointments"),
    path('Salon/Login/TodayAppointments/Export-CSV', views.exportcsv, name="export-csv"),
    path('Salon/Login/TodayAppointments/Export-Excel', views.exportexcel, name="exportexcel"),
    path('Salon/Login/TodayAppointments/Export-PDF', views.exportpdf, name="exportpdf"),
    path('Salon/Login/Bookings/UpdateStatus/<ids>', views.statusupdate, name="statusupdate"),
    path('User/Login/UserHomePage', views.userhome, name="userhome"),
    path('User/Login/HomePage', views.userhomepay, name="userhomepay"),
    path('User/Login/SalonAppointment/<id>', views.booking, name="booking"),
    path('User/Login/SalonAppointmentSubmit/<id>', views.appsubmit, name="appsubmit"),
    path('User/Login/Appointment/Payment/', views.payment, name="payment"),
    path('User/Login/Appointment/BankPayment/<id>', views.pay, name="pay"),
    path('User/Login/Appointment/BankPayment/card/<id>', views.card, name="card"),
    path('Logout', views.logouts, name="logouts"),
    path('Reviews/<id>', views.reviewss, name="reviews"),
    path('AddReview/<id>', views.addreviews, name="addreviews"),
    path('Review_Form/<id>', views.submitreviews, name="submitreviews"),
    path('User/Forgot_Password', views.user_forgot_password, name="ufpassword"),
    path('User/Forgot_Password_Reset', views.user_forgot_password_reset, name="ufpasswordreset"),
    path('Salon/Forgot_Password', views.salon_forgot_password, name="sfpassword"),
    path('Salon/Forgot_Password_Reset', views.salon_forgot_password_reset, name="sfpasswordreset"),
    ]