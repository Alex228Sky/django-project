from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Books(models.Model):
    image = models.FileField(null=True, blank=True)
    book = models.CharField(max_length=120)
    dis = models.CharField(max_length=120)
    cont = models.CharField(max_length=130)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)



