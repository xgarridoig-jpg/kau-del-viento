from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

urlpatterns = [
    path("products/", ProductoListView.as_view(), name="product_list"),
    path("products/create/", ProductoCreateView.as_view(), name="product_create"),
    path("products/edit/<int:pk>/", ProductoUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductoDeleteView.as_view(), name="product_delete"),
]
