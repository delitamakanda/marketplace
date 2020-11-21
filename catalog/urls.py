from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-list/<slug:category_slug>/',
         views.product_list, name='product_list_by_category'),
    path('product-detail/<int:id>/<slug:slug>/',
         views.product_detail, name='product_detail'),
]
