from django.db import models

__all__ = ['Property']


class Property(models.Model):
    """
    Reprecent a home propetie
    """
    address = models.CharField(max_length=255)
    available = models.BooleanField()
    coordinates = models.CharField(max_length=255)  # x,y para google maps
    description = models.CharField(max_length=255)
    services = models.CharField(max_length=50)  # choices=[luz, gas, natural, cochera]

    def __srt__(self):
        return f"Propiedad: {self.id}"
