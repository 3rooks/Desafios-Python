from django.urls import path
from pythonapp import views

urlpatterns = [
    path('', views.index),
]
