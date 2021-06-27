from django.db import models
from properties.constants import StateChoices, HomeType

__all__ = ['Property']


class PropertyImages(models.Model):
    """
    Reprecent all images for a property.
    """
    image = models.ImageField(
        upload_to='propiedades', blank=True, null=True,
    )
    prop = models.ForeignKey(
        "Property",
        related_name="images",
        on_delete=models.CASCADE,
    )


class Property(models.Model):
    """
    Reprecent a home property.
    """
    address = models.CharField(max_length=255, null=True)
    available = models.BooleanField(default=True)
    coordinates = models.CharField(max_length=255, blank=True, null=True)  # x,y para google maps
    description = models.CharField(max_length=255, null=True)
    services = models.CharField(max_length=50, blank=True, null=True)  # choices=[luz, gas, natural, cochera]

    home_type = models.PositiveSmallIntegerField(
        choices=HomeType.CHOICES,
        default=HomeType.HOUSE,
    )
    rooms = models.PositiveSmallIntegerField(null=True, default=1)
    bathroom = models.PositiveSmallIntegerField(null=True, default=1)
    bedroom = models.PositiveSmallIntegerField(null=True, blank=True)
    garage = models.BooleanField(default=False)
    total_surface = models.PositiveSmallIntegerField(null=True, blank=True)
    covered_area = models.PositiveSmallIntegerField(null=True, blank=True)
    state = models.PositiveSmallIntegerField(
        choices=StateChoices.CHOICES,
        default=StateChoices.VERY_GOOD,
    )
    ages = models.PositiveSmallIntegerField(blank=True)
    amount = models.IntegerField(blank=False)

    def __srt__(self):
        return f"Propiedad: {self.id}"
