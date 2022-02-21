from django.contrib import admin
from django.db import models
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=15, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name