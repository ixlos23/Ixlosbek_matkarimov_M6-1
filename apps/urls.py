from django.contrib.auth.views import LoginView
from django.urls import path, include

from apps.views import RegisterFormView, LoginTemplateView

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='home'),
    path('login', LoginView.as_view(template_name='apps/login.html'), name='login'),
    path('products', LoginView.as_view(template_name='apps/product-list.html'), name='products'),
    path('register', RegisterFormView.as_view(), name='register'),
]