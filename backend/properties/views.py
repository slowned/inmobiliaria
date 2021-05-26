from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from properties.models import Property
from properties.serializers import PropertiesSerializer

__all__ = ['PropertiesViewSet']


# class PropertiesViewSet(ReadOnlyModelViewSet):
class PropertiesViewSet(ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Property.objects.all()
