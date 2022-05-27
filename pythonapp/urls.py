from django.urls import path
from pythonapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search),
    path('topics/', views.rendertopic, name='topics'),
    path('contact/', views.contact, name='contact'),
    path('topic/', views.topicform, name='topic'),
]
