from django.db import models

# Create your models here.
class Store_Data(models.Model):
    name = models.CharField(max_length=122, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name