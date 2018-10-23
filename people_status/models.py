from django.db import models


# Create your models here1.

class person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_picture = models.FileField()

    def  __str__(self):
        return self.first_name+'-'+self.last_name


