# filmler/oneriler.py
# Not: İçindeki fonksiyonun adı DEĞİŞMEDİ!

from .models import Film, Puanlama, Etiket
from django.db.models import Count
from django.contrib.auth.models import User

def icerik_tabanli_tavsiye_et(user: User, limit=5):
    yuksek_puanli_filmler_id = Puanlama.objects.filter(
        kullanici=user, puan__gte=7
    ).values_list('film_id', flat=True)

    tercih_edilen_etiketler = Etiket.objects.filter(
        filmler__id__in=yuksek_puanli_filmler_id
    ).annotate(
        etiket_sayisi=Count('id')
    ).order_by('-etiket_sayisi')[:10]

    tavsiye_edilecek_filmler = Film.objects.filter(
        etiketler__in=tercih_edilen_etiketler
    ).exclude(
        id__in=yuksek_puanli_filmler_id 
    ).annotate(
        tavsiye_skoru=Count('etiketler')
    ).order_by('-tavsiye_skoru', '-yayin_tarihi')

    return tavsiye_edilecek_filmler[:limit]