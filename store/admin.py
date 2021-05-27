from django.contrib import admin
from .models import product

# Register your models here.
class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display =  ('product_name','price','stock','created_date','modified_date','is_available')

admin.site.register(product, productAdmin)
