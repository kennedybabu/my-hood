from django.db import models

# Create your models here.


class Hood(models.Model):
    #host =
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True)
    # occupants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


