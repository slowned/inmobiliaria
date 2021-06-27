from rest_framework.serializers import ModelSerializer

from properties.models import Property, PropertyImages

__all__ = ['PropertiesSerializer']


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = ['image']

class PropertiesSerializer(ModelSerializer):
    images = ImagesSerializer()

    class Meta:
        model = Property
        fields = [
            'images',
            'address',
            'ages',
            'amount',
            'bathroom',
            'bedroom',
            'covered_area',
            'coordinates',
            'description',
            'garage',
            'home_type',
            'rooms',
            'total_surface',
            'state',
            'services',
        ]

    # def create(self, validated_data):
    #     import ipdb;ipdb.set_trace()
    #     instance = Property.objects.create(**validated_data)
    #     PropertyImages.objects.create(image=image, Equipment=instance)
    #     return instance

    # def to_representation(self, instance):
    #     representation = super(EquipmentSerializer, self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
    #     return representation 

    def create(self, validated_data):
        image_validated_data = validated_data.pop('images')
        instance = Property.objects.create(**validated_data)
        image_set_serializer = self.fields['images']
        import ipdb;ipdb.set_trace()
        # crear imagen y setearle la propiedad



        for image in image_validated_data:
            image['prop'] = instance
        image = image_set_serializer.create(image_validated_data)
        return instance
