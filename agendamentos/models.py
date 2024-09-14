from django.db import models

# Modelo Agendamento
# Este modelo representa um agendamento de pagamento com vários campos para armazenar informações como data,
# recorrência, detalhes da conta bancária e valor do pagamento.
class Agendamento(models.Model):
    # Campo para armazenar a data do pagamento
    data_pagamento = models.DateField()
    
    # Campo booleano para indicar se o agendamento permite recorrência
    permite_recorrencia = models.BooleanField(default=False)
    
    # Campo para armazenar a quantidade de recorrências (opcional)
    quantidade_recorrencia = models.IntegerField(null=True, blank=True)
    
    # Campo para armazenar o intervalo entre as recorrências, em dias (opcional)
    intervalo_recorrencia = models.IntegerField(null=True, blank=True)
    
    # Campo para armazenar o status da recorrência (opcional)
    status_recorrencia = models.CharField(max_length=50, blank=True, null=True)
    
    # Campo para armazenar o número da agência bancária
    agencia = models.IntegerField()
    
    # Campo para armazenar o número da conta bancária
    conta = models.IntegerField()
    
    # Campo para armazenar o valor do pagamento
    # max_digits define o número máximo de dígitos, incluindo os decimais
    # decimal_places define o número de casas decimais
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)

    # Sobrescrevendo o método save
    def save(self, *args, **kwargs):
        # Converter valor_pagamento para inteiro antes de salvar no banco de dados
        self.valor_pagamento = int(self.valor_pagamento)
        # Chama o método save original da superclasse (models.Model)
        super().save(*args, **kwargs)

    # Método __str__
    # Define a representação em string do objeto, útil para exibição no Django admin e em outras situações
    def __str__(self):
        return f"Agendamento {self.id} - {self.data_pagamento}"