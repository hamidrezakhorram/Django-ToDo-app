from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user (self , email , password , **extra_fields):
        if not email :
            raise ValueError (_("The Email must be set"))
        email = self.normalize_email(email)
        user =self.model(email= email , **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self , email , password,**extra_fields):
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_active' , True)
        if (extra_fields.get('is_staff') != True):
            raise ValueError(_("Superuser must have is_staff=True."))
        if (extra_fields.get('is_superuser') != True):
            raise ValueError(_("Superuser must have is_staff=True."))
        
        return self.create_user(email , password ,**extra_fields )
    
    

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250 , unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)
    
    def __str__(self):
        return self.email

    