from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.doctorHome),
    path('login', views.doctorLogin)
]