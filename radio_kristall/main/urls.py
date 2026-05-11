from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news'),
    path('vacancies/', views.vacancies_list, name='vacancies'),
    path('about/', views.about, name='about'),
]