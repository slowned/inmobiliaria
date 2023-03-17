import base64

from rest_framework import status

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser

from properties.models import Property, PropertyImages
from properties.serializers import PropertiesSerializer
# from properties.filters import PropertyFilterSet

__all__ = ['PropertiesViewSet']


class PropertiesViewSet(ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Property.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    # http_method_names = ['get']
    # filterset_class = PropertyFilterSet

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
