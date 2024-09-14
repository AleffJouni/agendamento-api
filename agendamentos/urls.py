from django.urls import path
from .views import AgendamentoCreateAPIView, AgendamentoListAPIView, AgendamentoDetailAPIView, AgendamentoDeleteAPIView, home

# Definindo as URLs da aplicação 'agendamentos'
urlpatterns = [
    # Rota para a página inicial. Quando o usuário acessa a URL raiz ('/'), a função 'home' é chamada.
    # Esta função retorna uma resposta simples, informando que a API está funcionando.
    path('', home, name='home'),
    
    # Rota para criar um novo agendamento. Esta rota utiliza o método HTTP POST.
    # Endpoint: /api/agendamentos/
    # Exemplo de uso: POST http://127.0.0.1:8000/api/agendamentos/
    path('api/agendamentos/', AgendamentoCreateAPIView.as_view(), name='create-agendamento'),
    
    # Rota para listar todos os agendamentos. Esta rota utiliza o método HTTP GET.
    # Endpoint: /api/agendamentos/list/
    # Exemplo de uso: GET http://127.0.0.1:8000/api/agendamentos/list/
    path('api/agendamentos/list/', AgendamentoListAPIView.as_view(), name='list-agendamentos'),
    
    # Rota para consultar os detalhes de um agendamento específico pelo ID. Esta rota utiliza o método HTTP GET.
    # O parâmetro <int:pk> representa o ID do agendamento a ser consultado.
    # Endpoint: /api/agendamentos/<id>/
    # Exemplo de uso: GET http://127.0.0.1:8000/api/agendamentos/1/
    path('api/agendamentos/<int:pk>/', AgendamentoDetailAPIView.as_view(), name='detail-agendamento'),
    
    # Rota para excluir um agendamento específico pelo ID. Esta rota utiliza o método HTTP DELETE.
    # O parâmetro <int:pk> representa o ID do agendamento a ser excluído.
    # Endpoint: /api/agendamentos/<id>/delete/
    # Exemplo de uso: DELETE http://127.0.0.1:8000/api/agendamentos/1/delete/
    path('api/agendamentos/<int:pk>/delete/', AgendamentoDeleteAPIView.as_view(), name='delete-agendamento'),
]