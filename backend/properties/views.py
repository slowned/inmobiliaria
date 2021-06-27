from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from properties.models import Property
from properties.serializers import PropertiesSerializer
from properties.filters import PropertyFilterSet

__all__ = ['PropertiesViewSet']


class PropertiesViewSet(ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Property.objects.all()
    # http_method_names = ['get']
    filterset_class = PropertyFilterSet

    def list(self, request, *args, **kwargs):
        # import ipdb;ipdb.set_trace()
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
