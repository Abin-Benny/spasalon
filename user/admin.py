from django.contrib import admin
from .models import contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Email')
    readonly_fields = ('First_name', 'Last_name','Email','Subject','Message')

admin.site.register(contact,contactAdmin)



