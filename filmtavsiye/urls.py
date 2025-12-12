# filmtavsiye/urls.py

from django.contrib import admin
from django.urls import path, include # 'include' metodu import edilmiş olmalı

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ana sayfa (root) isteğini filmler uygulamasına yönlendiriyor
    path('', include('filmler.urls')), 
]