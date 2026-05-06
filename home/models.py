from datetime import date
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    birth = models.DateField()
    mother_name = models.CharField(max_length=255)
    ip = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.username} | {self.birth.strftime("%d-%m-%Y")}"
    
    def yearsOld(self):
        now = date.today()
        age = now.year - self.birth.year - ((now.month, now.day) < (self.birth.month, self.birth.day)) 
        return f"{self.username} tem {age} anos"
