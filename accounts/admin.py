from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

class UsersAdmin(UserAdmin):
    """
    This allows the passwords to be hashed and makes the admin panel more secure
    """
    
    ordering = ['id']
    list_display=['username','email']
    list_filter = []

    fieldsets = (
        (None, {'fields': ( 'email', 'username', 'password', 'phone_number', 'firstname', 'lastname', 'location', 'address', 'account_type', 'profile_photo')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

    search_fields =  ('username', 'email')
    ordering = ('username','email')

    filter_horizontal = ()

# Register your models here.
admin.site.register(Users, UsersAdmin)
