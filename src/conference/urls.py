from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('welcome',welcome, name='welcome'),
    path('view_paper',view_paper, name='view_paper'),
    path('view_paper/<int:pk>/detail',view_detail, name='view_detail'),
    re_path('view_paper/(?P<pk>\d+)/detail/delete',delete_paper, name='delete_paper'),
    path('submit_paper',submit_paper, name='submit_paper'),
]