from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False) 
    curso = models.CharField(max_length=100, null=False, blank=False)
    turma = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nome
    
    



# Create your models here.
