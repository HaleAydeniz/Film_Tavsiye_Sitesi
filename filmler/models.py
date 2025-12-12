from django.db import models
from django.contrib.auth.models import User

class Tur(models.Model):
    isim = models.CharField(max_length=50)
    
    def __str__(self):
        return self.isim

class Etiket(models.Model):
    isim = models.CharField(max_length=50)
    
    def __str__(self):
        return self.isim

class Film(models.Model):
    baslik = models.CharField(max_length=100)
    ozet = models.TextField()
    yonetmen = models.CharField(max_length=100)
    yayin_tarihi = models.DateField()
    # Hata veren eksik alan buydu, ekledik:
    afis_url = models.CharField(max_length=250, blank=True, null=True, help_text="Afiş resminin linki")
    
    # İlişkiler
    turler = models.ManyToManyField(Tur)
    etiketler = models.ManyToManyField(Etiket)

    def __str__(self):
        return self.baslik

class Puanlama(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    puan = models.IntegerField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.username} - {self.film.baslik}"