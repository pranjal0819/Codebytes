from django.urls import path
from .views import *

urlpatterns = [
	path('email', email, name='email'),
	path('spreadingnumber',spreadingnumber, name='spreadingnumber'),
]