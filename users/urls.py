from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/blogs/', permanent=False), name='bloghome'),
    path('bloghome', RedirectView.as_view(url='/blogs/', permanent=False), name='bloghome'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]
