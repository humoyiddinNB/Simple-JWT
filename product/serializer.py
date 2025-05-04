from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSeralizer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['author']