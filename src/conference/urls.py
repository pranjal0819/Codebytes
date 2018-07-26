from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

	path('welcome', login_required(welcome.as_view()), name='welcome'),

    path('view_paper', login_required(view_paper.as_view()), name='view_paper'),

    path('submit_paper', login_required(submit_paper.as_view()), name='submit_paper'),

    #path('review_paper/<int:pk>', login_required(review_paper.as_view()), name='review_paper'),
    
    path('view_paper/<int:pk>/detail', login_required(view_detail.as_view()), name='view_detail'),

    path('view_paper/<int:pk>/delete', login_required(delete_paper.as_view()), name='delete_paper'),

    path('view_paper/<int:pk>/select', login_required(select_user.as_view()), name='select_user'),

    path('view_paper/<int:paper_pk>/select/<user_pk>', login_required(selected_user.as_view()), name='selected_user'),
]