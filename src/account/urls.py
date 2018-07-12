from django.urls import path
from .views import *

urlpatterns = [
	path('login',login, name='login'),
	path('signup',signup, name='signup'),
	path('logout',logout, name='logout'),
	path('profile',userprofile, name='userprofile'),
]