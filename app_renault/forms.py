from django import forms
from .models import Risco, Solucao, Piloto, Usuario

class RiscoForm(forms.ModelForm):
    class Meta:
        model = Risco
        fields = '__all__'

class SolucaoForm(forms.ModelForm):
    class Meta:
        model = Solucao
        fields = '__all__'