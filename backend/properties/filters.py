from django_filters import (
    FilterSet,
    ChoiceFilter,
    NumberFilter,
    BooleanFilter,
    CharFilter,
)

from properties.models import Property
from properties.constants import StateChoices, HomeType

__all__ = ['PropertyFilterSet']


class PropertyFilterSet(FilterSet):
    home_type = ChoiceFilter(
        field_name='home_type',
        choices=HomeType.CHOICES,
    )
    room = NumberFilter(field_name='rooms')
    bedroom = NumberFilter(field_name='bedroom')
    bathroom = NumberFilter(field_name='bathroom')
    price_max = NumberFilter(field_name='price', lookup_expr='lte')
    price_min = NumberFilter(field_name='price', lookup_expr='gte')
    garden = CharFilter(field_name='garden')
    garage = BooleanFilter(field_name='garage')

    class Meta:
        model = Property
        fields = []
