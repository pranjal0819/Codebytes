from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('email', email.as_view(), name='email'),
    path('spreadingnumber', TemplateView.as_view(template_name='spreading_number.html'), name='spreadingnumber'),
]
