from rest_framework import serializers

from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "order_number", "icon"]
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    # допомагає виводити категорію через виконання __str__
    # category = serializers.StringRelatedField()
    # виводить slug
    # category = serializers.SlugRelatedField(slug_field="slug", read_only=True)

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "image", "price", "category"]
        read_only_fields = ["id"]