from django.db import models
from django.contrib.auth.models import User

# models for custemers
class Custemer(models.Model):
     LIVE=1
     DELETE=0
     DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
     name=models.CharField(max_length=200)
     address=models.TextField()
     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='custemor_profile')
     phone=models.CharField(max_length=10)
     delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)

     def __str__(self) -> str:
         return self.name
