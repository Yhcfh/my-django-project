from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]