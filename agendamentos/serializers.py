from rest_framework import serializers
from .models import Agendamento

# Serializer para o modelo Agendamento
# Este serializer converte os objetos Agendamento para o formato JSON e valida os dados recebidos na API
class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento # Modelo associado ao serializer
        fields = '__all__' # Incluir todos os campos do modelo Agendamento