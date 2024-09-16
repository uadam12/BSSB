from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Banks
    path('banks/', views.banks, name='banks'),
    path('banks/<int:id>/update', views.update_bank, name='update-bank'),
    path('banks/<int:id>/delete', views.delete_bank, name='delete-bank'),
    
    # Local Government Area(LGA)
    path('lgas/', views.lgas, name='lgas'),
    path('lgas/<int:id>/update', views.update_lga, name='update-lga'),
    path('lgas/<int:id>/delete', views.delete_lga, name='delete-lga'),
    
    # Articles
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/update', views.update_article, name='update-article'),
    path('articles/<int:id>/delete', views.delete_article, name='delete-article'),
]
