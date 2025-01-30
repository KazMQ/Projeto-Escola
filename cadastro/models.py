from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100) 
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=50)
    #print(f"Aluno {nome} é do curso {curso} e faz parte da turma {turma}")#
    
    



# Create your models here.
