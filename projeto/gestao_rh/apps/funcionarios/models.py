from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos
from apps.empresa.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    #caso seja deletado um usuario, é deletado um funcionario
    #so vai existir um usuario por funcionario
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    #cria uma lista de departamentos
    departamentos = models.ManyToManyField(Departamentos)

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome
