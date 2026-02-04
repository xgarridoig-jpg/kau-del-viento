from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect_by_role(user)
    else:
        form = LoginForm(request)

    return render(request, "accounts/login.html", {"form": form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Cuenta creada correctamente. Ya puedes ingresar.")
            return redirect("accounts:login")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada.")
    return redirect("core:home")


def redirect_by_role(user):
    if user.is_staff:
        return redirect("dashboard:admin_home")
    return redirect("dashboard:user_home")
