# filmler/urls.py

from django.urls import path
from . import views

# Uygulama ismi tanımlama
app_name = 'filmler'

urlpatterns = [
    # Ana sayfa: Bütün filmleri listeleyecek
    path('', views.film_listesi, name='film_listesi'), 
    
    # Film detay sayfası: Kullanıcının puan verebileceği sayfa
    path('film/<int:pk>/', views.film_detay, name='film_detay'),
    
    # Tavsiye sonuçlarını gösterecek sayfa
    path('tavsiyelerim/', views.tavsiye_sonuclari, name='tavsiye_sonuclari'),
]