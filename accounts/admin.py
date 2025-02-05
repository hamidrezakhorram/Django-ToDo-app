from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model =User
    list_display =('email' ,)
    list_filter =('is_active' , 'is_staff' ,)
    search_fields = ('email' ,)
    ordering = ('email' ,)
    fieldsets = (
        ("Authenticate", {"fields": ("email", )}),
         ("premition", {"fields": ("is_active", "is_superuser","is_staff")}),
    
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active" )}
        ),
    )
    
    

admin.site.register(User , CustomUserAdmin)    