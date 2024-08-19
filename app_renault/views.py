from django.shortcuts import render
from rest_framework import viewsets
from .models import Risco, Usuario, Piloto, Solucao
#from .serializers import RiscoSerializer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import  RiscoForm


class CreateRisco(CreateView):
    model = Risco
    form_class = RiscoForm
    template_name = 'formulario_risco.html'
    success_url = reverse_lazy('listar_risco')


class RiscoList(ListView):
    model = Risco
    template_name = 'listar_risco.html'

class RiscoUpdate(UpdateView):
    model = Risco
    fields = ['descricao', 'tipo', 'probabilidade', 'area', 'classificacao', 'projeto', 'data_entrada', 'impacto', 'consequencia', 'jalon_afetado',
    'metier', 'status', 'id_usuario']
    template_name = 'formulario_risco.html'
    success_url = reverse_lazy('listar_risco')

class RiscoDelete(DeleteView):
    model = Risco
    template_name = 'listar_risco.html'
    success_url = reverse_lazy('listar-risco')

