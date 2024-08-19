from django.urls import path, include
from .views import CreateRisco, RiscoList, RiscoUpdate, RiscoDelete


urlpatterns =[
  #path('CreateOportunity/', CreateOportunity.as_view(), name="cadastrar-oportunidade"),  
  path('CreateRisco/', CreateRisco.as_view(), name="RiscoForm"),
  path('', RiscoList.as_view(), name="listar-risco"),
  path('RiscoUpdate/<int:pk>/', RiscoUpdate.as_view(), name="editar-risco"),
  path('RiscoDelete/<int:pk>/', RiscoDelete.as_view(), name="deletar-risco"),
  
]
   