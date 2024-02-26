from django.urls import path
from . import views

urlpatterns = [
    path('', views.Responserequested, name='home'),
]
