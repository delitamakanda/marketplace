import django_filters.rest_framework

from rest_framework import filters, generics
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

from .filters import ProductFilter
from ..models import Product, Category
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductCreateUpdateSerializer,
)

from .pagination import CategoryPagination


class APIRoot(APIView):

    def get(self, request, format=None):
        data = {
            'products': {
                'count': Product.objects.all().count(),
                'url': api_reverse('products_api', request=request)
            },
            'category': {
                'count': Category.objects.all().count(),
                'url': api_reverse('category_api', request=request)
            },
            'auth': {
                'login':  api_reverse("jwt", request=request),
                'refresh':  api_reverse("refresh", request=request),
            },
        }
        return Response(data)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['description', 'name']
    ordering_fields = ['id', 'name']
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filter_class = ProductFilter


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = (IsAdminUser,)


class ProductDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = (IsAdminUser,)
