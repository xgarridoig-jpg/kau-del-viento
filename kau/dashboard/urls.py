from django.urls import path
from . import views
from .views import UserListView

app_name = "dashboard"

urlpatterns = [
    path("admin/", views.admin_home, name="admin_home"),
    path("usuario/", views.user_home, name="user_home"),
    path("usuarios/", UserListView.as_view(), name="user_list"),
]
