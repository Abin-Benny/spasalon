from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active') # Display all the items given in this line in a single line
    list_display_links = ('email','first_name','last_name') # It provide links to all items given in this line to inner page
    readonly_fields = ('last_login','date_joined') # user only can read not edit or write the items given in this fields
    ordering = ('-date_joined',) # display items in descending order of date joined.
    filter_horizontal = () #this line and below two lines are used to display items provided in list_display in a single line
    list_filter = ()
    fieldsets=()
admin.site.register(Account,AccountAdmin)
