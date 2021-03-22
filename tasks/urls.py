from django.urls import path
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from econet import settings


urlpatterns = [
    path('', views.taskHome),
]
