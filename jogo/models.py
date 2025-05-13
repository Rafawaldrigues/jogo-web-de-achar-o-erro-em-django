from django.db import models

class Phase(models.Model):
    number = models.PositiveIntegerField(unique=True)
    image = models.ImageField(upload_to='phases/')
    object_x = models.PositiveIntegerField()
    object_y = models.PositiveIntegerField()
    tolerance = models.PositiveIntegerField(default=50)