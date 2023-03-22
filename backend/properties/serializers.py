from io import BytesIO
from django.core.files import File
from rest_framework.serializers import ModelSerializer, ImageField
from PIL import Image

from properties.models import Property, PropertyImages

__all__ = ['PropertiesSerializer', 'ImagesSerializer']


class ImagesSerializer(ModelSerializer):
    image = ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = PropertyImages
        fields = ['image']


class PropertiesSerializer(ModelSerializer):
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = Property
        fields = [
            'id',
            'images',
            'address',
            'expenses',
            # 'ages',
            # 'amount',
            # 'bathroom',
            # 'bedroom',
            # 'covered_area',
            # 'coordinates',
            # 'description',
            # 'garage',
            'home_type',
            # 'rooms',
            # 'total_surface',
            # 'state',
            # 'services',
        ]

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images[]')

        property_instance = Property.objects.create(**validated_data)

        for image_data in images_data:
            #TODO: usar ImagesSerializer create
            PropertyImages.objects.create(
                prop=property_instance,
                image=image_data,
            )

        return property_instance

    # TODO: no se esta usando
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
