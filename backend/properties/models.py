import os

from io import BytesIO
# from PIL import  Image

from django.core.files import File
from django.db import models

from properties.constants import StateChoices, HomeType, Services

__all__ = ['Property', 'PropertyImages']


def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


def get_image_path(instance, filename):
    """
    generate relative path bases on propoperty id
    """
    return os.path.join('propiedades', str(instance.prop.id) + '/' + filename)


class PropertyImages(models.Model):
    """
    Reprecent all images for a property.
    """
    image = models.ImageField(
        upload_to=get_image_path, blank=True, null=True,
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
    expensas = models.PositiveSmallIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    home_type = models.PositiveSmallIntegerField(
        choices=HomeType.CHOICES,
        default=HomeType.HOUSE,
    )
    # available = models.BooleanField(default=True)
    # coordinates = models.CharField(max_length=255, blank=True, null=True)  # x,y para google maps
    # description = models.CharField(max_length=255, null=True, blank=True)
    # services = models.CharField(
    #     max_length=255, blank=True, null=True)  # [luz, gas, natural, cochera]
    # rooms = models.PositiveSmallIntegerField(null=True, default=1)
    # bathroom = models.PositiveSmallIntegerField(null=True, default=1)
    # bedroom = models.PositiveSmallIntegerField(null=True, blank=True)
    # garage = models.BooleanField(default=False)
    # total_surface = models.PositiveSmallIntegerField(null=True, blank=True)
    # covered_area = models.PositiveSmallIntegerField(null=True, blank=True)
    # state = models.PositiveSmallIntegerField(
    #     choices=StateChoices.CHOICES,
    #     default=StateChoices.VERY_GOOD,
    # )
    # ages = models.PositiveSmallIntegerField(blank=True)
    # amount = models.IntegerField(blank=False)
    # price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __srt__(self):
        return f"Propiedad: {self.id}"

    # definir get services spliteados x ,




# CODIGO PARA AGREGAR MULTIPLES IMAGES DEL ADMIN NO SIRVE
# class MyModelImage(models.Model):
#     building = models.ForeignKey(
#         "Property",
#         on_delete=models.CASCADE,
#         related_name="img",
#     )
#     image = models.ForeignKey(
#         "Image",
#         on_delete=models.CASCADE
#     )


# class Image(models.Model):
#     img = models.ImageField(upload_to="images/")


