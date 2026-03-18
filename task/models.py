from django.db import models

class TaskModels(models.model):
    class Status(models.TextChoices):
        AGUARDANDO_ANALISE = 'aguardando_analise', 'Aguardando análise'
        ABERTO = 'aberto', 'Aberto'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        AGUARDANDO_TERCEIROS = 'aguardando_teceiros', 'Aguardando terceiros' 
        CANCELADO = 'cancelado', 'Cancelado'
        FINALIZADO = 'finalizado', 'Finalizado'
    
    class Priority(models.TextChoices):
        INDEFINIDA = 'indefinida', 'Indefinida'
        BAIXA = 'baixa', 'Baixa'
        MEDIA = 'media', 'Média'
        ALTA = 'alta', 'Alta'

    description = models.TextField(max_length=255)
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.AGUARDANDO_ANALISE
    )
    
    priority = models.TextField(
        max_length=15,
        choices=Priority.choices,
        default=Priority.INDEFINIDA,
    )

    #userOpening
    #userOperate
    #departament