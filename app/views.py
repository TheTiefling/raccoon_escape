from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class EnviarcomentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'enviarcoment.html')
    def post(self, request):
        pass
class PerfilView(View):
    def get(self, request, *args, **kwargs):
        perfis = Usuario.objects.all().order_by('-data_logado').first()
        return render(request, 'perfil.html', {'perfil': perfis})
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        if nome and email and idade:
            Usuario.objects.create(nome=nome, email=email, idade=idade)
        return redirect('perfil')
class ForumView(View):
    def get(self, request, *args, **kwargs):
        comentarios = Comentario.objects.all().order_by('-data_criacao')
        return render(request, 'forum.html', {'comentarios': comentarios})
    def post(self, request):
        nome = request.POST.get('nome')
        jogo = request.POST.get('jogo')
        comentario_texto = request.POST.get('comentario')
        if nome and jogo and comentario_texto:
            Comentario.objects.create(nome=nome, jogo=jogo, texto=comentario_texto)
        return redirect('forum')
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        idade = request.POST.get('idade')

        if not nome or not email or not senha or not idade:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')

        try:
            idade = int(idade)
        except ValueError:
            messages.error(request, 'Idade deve ser um número válido.')
            return redirect('login')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('login')
        
        try:
            usuario = Usuario.objects.create(
                nome=nome,
                email=email,
                senha=senha,
                idade=idade
            )
            usuario.save()

            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('index')

        except Exception as e:
            messages.error(request, f'Ocorreu um erro: {e}')
            return redirect('login')