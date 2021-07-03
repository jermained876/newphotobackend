from rest_framework.serializers import ModelSerializer
from carousel.models import Carousel


class CarouselSerializer(ModelSerializer):
    class Meta:
        model = Carousel
        fields ='__all__'
