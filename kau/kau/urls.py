from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from dashboard.views import dashboard_403


def error_403_view(request, exception=None):
    return render(request, "403.html", status=403)


def error_404_view(request, exception):
    return render(request, "404.html", status=404)


handler403 = error_403_view
handler404 = error_404_view
handler403 = dashboard_403

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("cart/", include("cart.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
