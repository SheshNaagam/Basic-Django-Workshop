from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name = "home"),
    path('about/', views.AboutPageView.as_view(), name = "about"),
    path('contact-us/', views.ContactPageView.as_view(), name = "contact"),
]
