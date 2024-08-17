from django.urls import path
from . import views

urlpatterns = [
    path('wel', views.home_view, name='wel')
]