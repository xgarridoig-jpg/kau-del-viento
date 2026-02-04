from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("admin/", views.admin_home, name="admin_home"),
    path("usuario/", views.user_home, name="user_home"),
]
