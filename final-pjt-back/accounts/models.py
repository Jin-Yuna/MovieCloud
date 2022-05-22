from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    kakao_id = models.IntegerField(null=True)  
    nickname = models.CharField(max_length=50, null=True)    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
