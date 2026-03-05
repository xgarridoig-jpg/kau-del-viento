from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="detail"),
    path("add/", views.cart_add, name="add"),
    path("remove/", views.cart_remove, name="remove"),
    path("remove-ajax/", views.cart_remove_ajax, name="remove_ajax"),
    path("update-ajax/", views.cart_update_ajax, name="update_ajax"),
    path("side/", views.side_cart, name="side"),
    path("clear/", views.cart_clear, name="clear"),
]