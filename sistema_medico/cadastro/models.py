from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    medico = models.CharField(max_length=100)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.medico} em {self.data}"
