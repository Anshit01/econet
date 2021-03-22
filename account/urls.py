from django.urls import path
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from econet import settings


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    # path('register/', views.Register.as_view(), name='signup'),
]