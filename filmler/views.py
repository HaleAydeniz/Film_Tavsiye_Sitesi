# filmler/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .models import Film, Puanlama
from .forms import PuanlamaForm
# Bu satır en kritik satırdır! Dosya adı doğru olmalıdır.
from .oneriler import icerik_tabanli_tavsiye_et


# 1. Bütün Filmleri Listeleme (Ana Sayfa)
def film_listesi(request):
    """Bütün filmleri ortalama puanlarına göre sıralar."""
    
    # Ortalama puanı hesaplayıp filmleri puana göre sıralıyoruz
    filmler = Film.objects.annotate(
        ortalama_puan=Avg('puanlama__puan')
    ).order_by('-ortalama_puan')
    
    context = {
        'filmler': filmler
    }
    return render(request, 'filmler/film_listesi.html', context)


# 2. Film Detay Sayfası ve Puanlama İşlemi
@login_required 
def film_detay(request, pk):
    """Tek bir filmin detayını gösterir ve kullanıcıdan puan alır."""
    
    film = get_object_or_404(Film, pk=pk)
    
    # Kullanıcının daha önce bu filme verdiği puanı çekme
    kullanici_puani = Puanlama.objects.filter(
        kullanici=request.user, 
        film=film
    ).first()

    if request.method == 'POST':
        form = PuanlamaForm(request.POST)
        if form.is_valid():
            puan_degeri = form.cleaned_data['puan']
            
            if kullanici_puani:
                # Eğer daha önce puan vermişse, puanı güncelle
                kullanici_puani.puan = puan_degeri
                kullanici_puani.save()
            else:
                # İlk kez puan veriyorsa, yeni puan oluştur
                Puanlama.objects.create(
                    kullanici=request.user,
                    film=film,
                    puan=puan_degeri
                )
            return redirect('filmler:film_detay', pk=film.pk) 

    else:
        # GET isteği: Formu yükle
        initial_data = {'puan': kullanici_puani.puan} if kullanici_puani else {}
        form = PuanlamaForm(initial=initial_data)

    # Film için genel ortalama puanı hesaplama
    ortalama_puan_hesapla = film.puanlama_set.aggregate(Avg('puan'))
    ortalama_puan = ortalama_puan_hesapla.get('puan__avg')

    context = {
        'film': film,
        'form': form,
        'kullanici_puani': kullanici_puani,
        'ortalama_puan': ortalama_puan
    }
    return render(request, 'filmler/film_detay.html', context)


# 3. Tavsiye Sonuçları Sayfası
@login_required
def tavsiye_sonuclari(request):
    """Kullanıcının puanlarına göre filmleri tavsiye eder."""
    
    # Tavsiye algoritması (tavsiye_algoritmasi.py'den çağrılır)
    tavsiyeler = icerik_tabanli_tavsiye_et(request.user)
    
    context = {
        'tavsiyeler': tavsiyeler
    }
    return render(request, 'filmler/tavsiye_sonuclari.html', context)