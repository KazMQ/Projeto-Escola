from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Aluno

def aluno_list(request):
       aluno_list = Aluno.objects.all()
       return render(request, 'cadastro/contato.html', {'alunos': aluno_list})

def show(request):
     return render(request, 'cadastro/show.html')

def base(request):
     return render (request, 'cadastro/base.html')

# Create your views here.
