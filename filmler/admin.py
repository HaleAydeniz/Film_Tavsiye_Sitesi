# filmler/admin.py (GEÇİCİ HALİ)
from django.contrib import admin
from .models import Tur, Etiket, Film, Puanlama 

# --- SİSTEMİ TEMİZLEME (Hata önleyici) ---
if admin.site.is_registered(Film): admin.site.unregister(Film)
if admin.site.is_registered(Tur): admin.site.unregister(Tur)
if admin.site.is_registered(Etiket): admin.site.unregister(Etiket)
if admin.site.is_registered(Puanlama): admin.site.unregister(Puanlama)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yayin_tarihi', 'yonetmen', 'afis_url') # <-- Buraya geri ekle
    list_filter = ('turler', 'etiketler')
    search_fields = ('baslik', 'ozet')
@admin.register(Tur)
class TurAdmin(admin.ModelAdmin):
    list_display = ('isim',)

@admin.register(Etiket)
class EtiketAdmin(admin.ModelAdmin):
    list_display = ('isim',)

@admin.register(Puanlama)
class PuanlamaAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'film', 'puan', 'tarih')