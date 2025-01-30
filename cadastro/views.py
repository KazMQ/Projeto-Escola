from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def contato(request):
    template = loader.get_template("contato.html")
    return HttpResponse(template.render())


def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def nome(request):
    print = None
    if request.method == 'POST':
        print = request.POST.get('nome')
    return render (request, "inicio.html", {'nome':nome})
def curso(request):
    curso = None
    if request.method == 'POST':
        materia = request.POST.get('curso')
    return render (request, "inicio.html", {'curso':curso})
def turma(request):
    turma = None
    if request.method == 'POST':
        turma = request.POST.get('turma')
    return render (request, "inicio.html", {'turma':turma})
# Create your views here.
