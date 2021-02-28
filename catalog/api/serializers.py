from rest_framework import serializers

from ..models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'created',
            'updated',
            'stock',
            'category',
        ]

class ProductCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'name',
            'image',
            'description',
            'price',
            'available',
            'created',
            'updated',
            'stock',
            'category',
        ]
