from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


# Create your views here.


def index(request):
    return HttpResponse('<h1>main</h1>')


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get("category_slug")
        if slug:
            products = Product.objects.filter(is_available=True, category__slug=slug)
        else:
            products = Product.objects.filter(is_available=True)
        return products

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    model = Product
    queryset = Product.objects.all()