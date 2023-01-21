from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordsChangeView

urlpatterns = [
    path('', views.index, name='index'),
    path('member/', views.member, name='member'),
    path('capacity/', views.capacity, name='capacity'),
    path('select/', views.select, name='select'),
    path('select/loggedout_manual/', views.loggedout_manual, name='loggedout_manual'),
    path('select/selected/', views.selected, name='selected'),
    path('pas/', views.pas, name='pas'),
    path('pas/change_password/', PasswordsChangeView.as_view(template_name = 'change_password.html')),
    # path('userdata/', views.userdata, name='userdata'),
]
