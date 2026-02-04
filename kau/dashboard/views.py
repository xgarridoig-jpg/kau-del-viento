from django.shortcuts import render
from .decorators import admin_required, usuario_required


@admin_required
def admin_home(request):
    return render(request, "dashboard/admin_home.html")


@usuario_required
def user_home(request):
    return render(request, "dashboard/user_home.html")

def dashboard_403(request, exception=None):
    return render(request, "dashboard/403_dashboard.html", status=403)