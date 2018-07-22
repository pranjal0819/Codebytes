from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
	path('login',login.as_view(), name='login'),
	path('signup',signup.as_view(), name='signup'),
	path('logout',login_required(logout), name='logout'),
	path('profile',login_required(profile.as_view()), name='profile'),
	path('edit-profile',login_required(edit_profile.as_view()), name='edit_profile'),
	path('change-username',login_required(change_username.as_view()), name='change_username'),
	path('change-password',login_required(change_password.as_view()), name='change_password'),
]