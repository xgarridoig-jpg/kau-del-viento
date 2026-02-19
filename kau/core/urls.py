from django.urls import path
from . import views
from .views import ConsultasListView

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("contacto/", views.contacto, name="contacto"),
    path("dashboard/consultas/", ConsultasListView.as_view(), name="consultas_list"),
]
