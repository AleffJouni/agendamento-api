from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Agendamento
from .serializers import AgendamentoSerializer

# Função de visualização simples para a página inicial
# Esta função é chamada quando o usuário acessa a URL raiz ('/').
# Retorna uma resposta HTTP simples com uma mensagem de boas-vindas.
def home(request):
    return HttpResponse("Bem-vindo à API de Agendamentos!")

# View para criar um novo agendamento
# Esta view utiliza a classe APIView para criar agendamentos.
# Método HTTP: POST
# Endpoint: /api/agendamentos/
class AgendamentoCreateAPIView(APIView):
    def post(self, request):
        # Serializa os dados recebidos na requisição
        serializer = AgendamentoSerializer(data=request.data)
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva o agendamento no banco de dados
            serializer.save()
            # Retorna os dados do agendamento criado com o status 201 (Criado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Se os dados não forem válidos, retorna os erros com o status 400 (Requisição Inválida)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# View para listar todos os agendamentos
# Esta view utiliza a classe genérica ListAPIView para listar agendamentos.
# Método HTTP: GET
# Endpoint: /api/agendamentos/list/
class AgendamentoListAPIView(generics.ListAPIView):
    # Define o conjunto de objetos (queryset) a ser listado
    queryset = Agendamento.objects.all()
    # Define o serializer a ser utilizado para converter os objetos em JSON
    serializer_class = AgendamentoSerializer

# View para consultar um agendamento específico
# Esta view utiliza a classe genérica RetrieveAPIView para consultar um agendamento pelo ID.
# Método HTTP: GET
# Endpoint: /api/agendamentos/<id>/
class AgendamentoDetailAPIView(generics.RetrieveAPIView):
    # Define o conjunto de objetos (queryset) a ser consultado
    queryset = Agendamento.objects.all()
    # Define o serializer a ser utilizado para converter os objetos em JSON
    serializer_class = AgendamentoSerializer

# View para excluir um agendamento específico
# Esta view utiliza a classe genérica DestroyAPIView para excluir um agendamento pelo ID.
# Método HTTP: DELETE
# Endpoint: /api/agendamentos/<id>/delete/
class AgendamentoDeleteAPIView(generics.DestroyAPIView):
    # Define o conjunto de objetos (queryset) a ser excluído
    queryset = Agendamento.objects.all()
    # Define o serializer a ser utilizado para converter os objetos em JSON
    serializer_class = AgendamentoSerializer