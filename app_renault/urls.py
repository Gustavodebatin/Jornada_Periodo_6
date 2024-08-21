from django.urls import path, include
from .views import CreateRisco, RiscoList, RiscoUpdate, RiscoDelete, CreateSolucao, SolucaoList, SolucaoUpdate, SolucaoDelete, listar_itens


urlpatterns =[
  #path('CreateOportunity/', CreateOportunity.as_view(), name="cadastrar-oportunidade"),  
  path('CreateRisco/', CreateRisco.as_view(), name="RiscoForm"),
  path('risco/', RiscoList.as_view(), name="listar-risco"),
  path('RiscoUpdate/<int:pk>/', RiscoUpdate.as_view(), name="editar-risco"),
  path('RiscoDelete/<int:pk>/', RiscoDelete.as_view(), name="deletar-risco"),

  path('CreateSolucao/', CreateSolucao.as_view(), name="SolucaoForm"),
  path('ListarSolucao', SolucaoList.as_view(), name="listar-solucao"),
  path('SolucaoUpdate/<int:pk>/', SolucaoUpdate.as_view(), name="editar-solucao"),
  path('SolucaoDelete/<int:pk>/', SolucaoDelete.as_view(), name="deletar-solucao"),
  path('', listar_itens, name='home'),
]
   