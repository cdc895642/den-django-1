
from django.urls import path
from . import views
from .models import Post
from .views import down
urlpatterns = [

    path('', views.HomePage,name='main-home'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add/', views.CreateNewsView.as_view(), name='news-add'),
    path('category/', views.category_game, name='category_game'),
    path('category_multi/', views.category_multi, name='category_multi'),
    path('file/<pk>/', down, name='down'),
]