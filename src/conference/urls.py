from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('welcome', welcome.as_view(), name='welcome'),
    path('submit_paper', login_required(submit_paper.as_view()), name='submit_paper'),
    path('view-all-paper', login_required(view_all_paper.as_view()), name='view_all_paper'),
    path('view-paper/<int:pk>/detail', login_required(view_detail.as_view()), name='view_detail'),
    path('view-paper/<int:pk>/delete', login_required(delete_paper.as_view()), name='delete_paper'),
    path('view-paper/<int:pk>/select-user', login_required(select_user.as_view()), name='select_user'),
    path('view-paper/<int:paper_pk>/select/<int:user_pk>', login_required(selected_user.as_view()), name='selected_user'),

    #path('review_paper/<int:pk>', login_required(review_paper.as_view()), name='review_paper'),
    #path('view_paper/<int:paper_pk>/deselect/<int:user_pk>', login_required(deselect_user.as_view()), name='deselect_user'),
]
