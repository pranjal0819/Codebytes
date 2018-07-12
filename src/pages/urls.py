from django.urls import path
from .views import *

urlpatterns = [
	path('spreadingnumber',spreadingnumber, name='spreadingnumber')
]