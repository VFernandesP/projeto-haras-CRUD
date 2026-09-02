from django.db import models

class Cavalo(models.Model):

    sexo_escolha = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=sexo_escolha)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    registro = models.CharField(max_length=50, unique=True)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(
            upload_to='cavalos_fotos/', 
            null=True, 
            blank=True,
            verbose_name='Foto do Cavalo'
        )

    def __str__(self):
        return f"{self.nome} ({self.sexo}) (R${self.valor})"

    class Meta:
        verbose_name = "Cavalo"
        verbose_name_plural = "Cavalos"
        ordering = ['nome']
