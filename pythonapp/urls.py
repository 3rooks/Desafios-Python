from django.urls import path
from pythonapp import views
app_name = 'pythonapp'
urlpatterns = [
    path('', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),

    path('home', views.TopicListView.as_view(), name='topic-list'),
    path('detail/<str:pk>', views.TopicDetailView.as_view(), name='topic-detail'),
    path('update/<str:pk>', views.TopicUpdateView.as_view(), name='topic-update'),
    path('delete/<str:pk>', views.TopicDeleteView.as_view(), name='topic-delete'),
    path('add/', views.TopicCreateView.as_view(), name='topic-add'),

    path('search/', views.Search),
]
