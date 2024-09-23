from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=40, verbose_name="Nome do usuário")
    email = models.CharField(max_length=40, verbose_name="E-mail do usuário")
    senha = models.CharField(max_length=40, unique=True,verbose_name="Senha do usuário")
    idade = models.IntegerField(verbose_name="Idade do usuário")
    
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}, {self.idade}"
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Admin(models.Model):
    nome = models.CharField(max_length=40, verbose_name="Nome do admin")
    email = models.CharField(max_length=40, verbose_name="E-mail do admin")
    senha = models.CharField(max_length=40, unique=True,verbose_name="Senha do admin")
    idade = models.IntegerField(verbose_name="Idade do admin")
    
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}, {self.idade}"
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
    
class Placar(models.Model):
    nome_exibicao = models.CharField(max_length=3, verbose_name="Nome de exibição do usuário")
    pontuacao = models.IntegerField(verbose_name="Pontuação do usuário")
    data_de_jogada = models.DateField(verbose_name="Data da Pontuação do usuário")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário que marcou o ponto")
    
    def __str__(self):
        return f"{self.nome_exibicao}, {self.pontuacao}, {self.data_de_jogada}"
    class Meta:
        verbose_name = "Placar"
        verbose_name_plural = "Placar"