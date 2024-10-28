from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=40, verbose_name="Nome do usuário")
    email = models.CharField(max_length=40, unique=True, verbose_name="E-mail do usuário")
    senha = models.CharField(max_length=128, verbose_name="Senha do usuário")
    idade = models.IntegerField(verbose_name="Idade do usuário")
    data_logado = models.DateTimeField(default=timezone.now, verbose_name="Data de Login")
    
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}, {self.idade}, {self.data_logado}"
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Comentario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do exibição")
    texto = models.TextField(verbose_name="Comentário do usuário")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    jogo = models.TextField(max_length=30, verbose_name="Nome do jogo")

    def __str__(self):
        return f'Comentário de {self.nome}'
    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Fóruns"