from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Attributes
    email = models.EmailField()
    prof_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username
