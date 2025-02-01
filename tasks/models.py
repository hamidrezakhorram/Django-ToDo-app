from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Task(models.Model):
    creator = models.ForeignKey( User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
