from django.contrib import admin

from owners.models import Owner

__all__ = ['OwnerAdmin']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"
