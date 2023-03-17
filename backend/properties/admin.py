from django.contrib import admin

from properties.models import Property, PropertyImages, MyModelImage, Image

# __all__ = ['PropertyAdmin', 'ImagesAdmin']


# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name = "Propiedad"
#         verbose_name_plural = "Propiedades"


# @admin.register(PropertyImages)
# class ImagesAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name = "Imagenes"


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "LAIMAGEN"


class MyModelImageInline(admin.StackedInline):
    model = MyModelImage
    extra = 1


class MyModelAdmin(admin.ModelAdmin):
    inlines = [MyModelImageInline]


admin.site.register(Property, MyModelAdmin)
