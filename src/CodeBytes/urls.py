"""CodeBytes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from pages.views import *
from conference.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('login',login, name='login'),
    path('signup',signup, name='signup'),
    path('logout',logout, name='logout'),
    path('feedback',feedback, name='feedback'),

    path('spreadingnumber',spreadingnumber, name='spreadingnumber'),

    path('welcome',welcome, name='welcome'),
    path('view_paper',view_paper, name='view_paper'),
    path('view_paper/<int:pk>/detail',view_detail, name='view_detail'),
    path('submit_paper',submit_paper, name='submit_paper'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
