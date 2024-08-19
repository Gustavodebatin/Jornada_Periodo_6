from django.db import models

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    token = models.CharField(max_length=255)

class Risco(models.Model):
    descricao = models.IntegerField()         
    tipo = models.CharField(max_length=255)
    probabilidade = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    classificacao = models.CharField(max_length=255)
    projeto = models.CharField(max_length=255)
    data_entrada = models.DateField()
    impacto = models.CharField(max_length=255)
    consequencia = models.CharField(max_length=255)
    jalon_afetado = models.CharField(max_length=255)
    metier = models.CharField(max_length=255)
    status = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='id', verbose_name="Usuário")
    

class Piloto(models.Model):
    nome = models.CharField(max_length=255)

class Solucao(models.Model):
    estrategia = models.CharField(max_length=255)
    probabilidade_residual = models.FloatField()
    impacto_residual = models.CharField(max_length=255)
    validacao_acao = models.CharField(max_length=255)
    data_alerta = models.DateField()
    nome_piloto = models.CharField(max_length=255)
    id_piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, to_field='id' )
    captalizacao = models.BooleanField()
    inicio_plano_acao = models.DateField()
    acao = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    data_resolucao = models.DateField()
    id_risco = models.ForeignKey(Risco, on_delete=models.CASCADE, to_field='id')

