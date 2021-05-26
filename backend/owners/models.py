from django.db import models

__all__ = ['Owner']


class Owner(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}, {self.surname}"
