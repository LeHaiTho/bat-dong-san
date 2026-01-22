from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('category/<slug:slug>/', views.news_category, name='news_category'),
    path('tag/<slug:slug>/', views.news_tag, name='news_tag'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
]
