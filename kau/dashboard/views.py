from django.shortcuts import render
from .decorators import admin_required, usuario_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView

@admin_required
def admin_home(request):
    return render(request, "dashboard/admin_home.html")


@usuario_required
def user_home(request):
    return render(request, "dashboard/user_home.html")

def dashboard_403(request, exception=None):
    return render(request, "dashboard/403_dashboard.html", status=403)

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class UserListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = User
    template_name = "dashboard/user_list.html"
    context_object_name = "usuarios"
    queryset = User.objects.all().order_by("-date_joined")
    paginate_by = 10