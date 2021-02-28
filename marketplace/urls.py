"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import (obtain_jwt_token,
                                      verify_jwt_token,
                                      refresh_jwt_token)

from catalog.api.views import (
    APIRoot,
    CategoryListAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductCreateAPIView,
    ProductDetailUpdateAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('catalog.urls', namespace='catalog')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += [
    path('api/', APIRoot.as_view(), name='api_root'),

    path('api/jwt/', obtain_jwt_token, name='jwt'),
    path('api/refresh/', refresh_jwt_token, name='refresh'),

    path('api/products/', ProductListAPIView.as_view(), name='products_api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(),
         name='products_detail_api'),
    path('api/products/new/', ProductCreateAPIView.as_view(), name='products_create_api'),
    path('api/products/<int:pk>/update/', ProductDetailUpdateAPIView.as_view(),
         name='products_detail_update_api'),

    path('api/categories/', CategoryListAPIView.as_view(), name='category_api'),
    path('api/categories/<int:pk>/', CategoryDetailAPIView.as_view(),
         name='category_detail_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
