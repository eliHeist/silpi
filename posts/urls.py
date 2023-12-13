from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostsView.as_view(), name='list'),
    path('<int:pk>/', views.PostView.as_view(), name='detail'),
]