from django.contrib.auth.models import User
from django.db import models


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
