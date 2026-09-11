from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<slug:slug>/update/', ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<slug:slug>/delete/', ProductDeleteAPIView.as_view()),
]
