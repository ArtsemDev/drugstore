from rest_framework.serializers import ModelSerializer

from main.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'descr', 'image', 'category')
