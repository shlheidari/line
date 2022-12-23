from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/', views.member, name='member'),
    path('capacity/', views.capacity, name='capacity'),
    path('select/', views.select, name='select'),
]
