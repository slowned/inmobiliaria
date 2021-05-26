from rest_framework.serializers import ModelSerializer

from properties.models import Property

__all__ = ['PropertiesSerializer']


class PropertiesSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'address',
            'coordinates',
            'description',
            'owner',
            'services',
        ]
