from django.urls import path
from .views import *

urlpatterns = [
	path('login',login, name='login'),
	path('signup',signup, name='signup'),
	path('logout',logout, name='logout'),
	path('profile',profile, name='profile'),
	path('profile/edit-username',edit_username, name='edit_username'),
	path('profile/edit-profile',edit_profile, name='edit_profile'),
	path('change-password',change_password, name='change_password'),
]