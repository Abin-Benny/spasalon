from django.urls import path
from . import views

urlpatterns=[
    path('Products/',views.products,name="shop_home"),
]