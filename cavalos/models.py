
from django.db import models
from django.utils import timezone


class Cavalo(models.Model):
    sexo_escolha = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Nascimento'
    )

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

    proprietario = models.ForeignKey(
        'Proprietario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cavalos',
        verbose_name='Proprietário'
    )

    def __str__(self):
        return f"{self.nome} ({self.sexo}) (R${self.valor})"

    class Meta:
        verbose_name = "Cavalo"
        verbose_name_plural = "Cavalos"
        ordering = ['nome']


class Proprietario(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Proprietário"
        verbose_name_plural = "Proprietários"
        ordering = ['nome']


class Veterinario(models.Model):
    nome = models.CharField(max_length=150)
    crmv = models.CharField(max_length=30, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nome} - CRMV {self.crmv}"

    class Meta:
        verbose_name = "Veterinário"
        verbose_name_plural = "Veterinários"
        ordering = ['nome']


class Atendimento(models.Model):
    cavalo = models.ForeignKey(
        Cavalo,
        on_delete=models.PROTECT,
        related_name='atendimentos'
    )

    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.PROTECT,
        related_name='atendimentos'
    )

    data = models.DateField(
        default=timezone.localdate,
        verbose_name='Data do atendimento'
    )

    descricao = models.TextField(verbose_name='Descrição')
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.cavalo.nome} - {self.data:%d/%m/%Y}"

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"
        ordering = ['-data']