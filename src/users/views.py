from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import UserRegisterForm

from django.views.generic.edit import CreateView


class SignUpView(SuccessMessageMixin, CreateView,LoginRequiredMixin):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
    error_message = 'Error in password or login (password must has at least 8 digits and symbols)'

    def form_invalid(self, form):
        messages.error(self.request, *form.errors.values())
        return super().form_invalid(form)


def logout(request):
    logout(request)
    return redirect('/')

