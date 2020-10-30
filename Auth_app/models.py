from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def on_delete():
    return

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=on_delete)
    portfolio = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_pic',blank = True)
    