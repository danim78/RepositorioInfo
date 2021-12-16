from django.shortcuts import render

from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Forms
from apps.users.forms import SignupForm


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'templates/users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('registerok')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'templates/users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'templates/users/logged_out.html'