from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


# Create your views here.
class AuthLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('index')


class AuthLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('index')


class AuthRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully. please log in."
    success_url = reverse_lazy('login')
