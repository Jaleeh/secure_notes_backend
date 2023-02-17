from django.db import models
from authentication.models import UserData
# Create your models here

class Note(models.Model):
    name = models.ForeignKey(UserData,on_delete= models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title