# filmler/forms.py

from django import forms
from .models import Puanlama

class PuanlamaForm(forms.ModelForm):
    puan = forms.IntegerField(
        label='Puanınız (1-10)',
        min_value=1, 
        max_value=10,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Puanlama
        fields = ['puan']