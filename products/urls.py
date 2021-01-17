from django.contrib import admin
from django.urls import path
from .views import ProductListView,ProductDetailView,ProductOptionListView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product-list'),
    path('detail/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('optiondetail/', ProductOptionListView.as_view(), name='product-option-detail')
]