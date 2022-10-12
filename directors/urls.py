from django.urls import path
from . import views
app_name='directors'

urlpatterns = [
    path('login',views.login_fun, name='check')
]