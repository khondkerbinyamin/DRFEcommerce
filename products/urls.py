from django.contrib import admin
from django.urls import path
from .views import ProductLisView,ProductDetailView

urlpatterns = [
    path('product/', ProductLisView.as_view(), name='product-list'),
    path('detail/<int:id>/', ProductDetailView.as_view(), name='product-detail')
]