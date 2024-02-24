from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.visitors_log, name='visitors_log'),
    path('add_visitor/', views.add_visitor, name='add_visitor'),
    path('admin/', views.admin, name='admin'),
]
