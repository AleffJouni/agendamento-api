from django.contrib import admin
from .models import Agendamento

# Registro do modelo Agendamento no painel de administração do Django
# Permite gerenciar os agendamentos através da interface de administração
admin.site.register(Agendamento)