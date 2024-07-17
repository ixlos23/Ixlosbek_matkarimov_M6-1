from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.forms import RegisterForm


class LoginTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    context_object_name = 'products'


class RegisterFormView(FormView):
    template_name = 'apps/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')