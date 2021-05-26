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
    owner = models.ForeignKey(
        'owners.Owner',
        on_delete=models.CASCADE,
        related_name="properties",
    )
    services = models.CharField(max_length=50)  # choices=[luz, gas, natural, cochera]
    tenant = models.CharField(max_length=100)  # FK a modelo inquilino

    def __srt__(self):
        return f"Propiedad: {self.id}"
