from django.db import models

# Create your models here.

class Visitors(models.Model):
    name = models.CharField(max_length= 200, default= None)
    email = models.EmailField(max_length= 245, default = None)

    def __str__(self):
        return self.name
    
