from django.shortcuts import render
from rest_framework import viewsets
from .models import Risco, Usuario, Piloto, Solucao, item
#from .serializers import RiscoSerializer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import  RiscoForm, SolucaoForm

#Risco
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

#Solucao
class CreateSolucao(CreateView):  
    model = Solucao
    form_class = SolucaoForm
    template_name = 'formulario_risco.html'
    success_url = reverse_lazy('listar-solucao')

class SolucaoList(ListView):
    model = Solucao
    template_name = 'listar_solucao.html'

class SolucaoUpdate(UpdateView):
    model = Solucao
    fields = ['estrategia', 'probabilidade_residual', 'impacto_residual', 'validacao_acao', 'data_alerta', 'nome_piloto', 'id_piloto', 'captalizacao', 'inicio_plano_acao', 'acao',
    'comentario', 'data_resolucao', 'id_risco']
    template_name = 'formulario_risco.html'
    success_url = reverse_lazy('listar-solucao')

class SolucaoDelete(DeleteView):
    model = Solucao
    template_name = 'listar_solucao.html'
    success_url = reverse_lazy('listar-solucao')

def listar_itens(request):
    itens = item.objects.all()  # Pega todos os objetos do modelo Item
    return render(request, 'home.html')

