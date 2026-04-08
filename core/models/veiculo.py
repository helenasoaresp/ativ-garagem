from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True
        )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True
    )
    acessorios = models.ManyToManyField(
        Acessorio, related_name='veiculos', blank=True
    )

    def __str__(self):
        return f"({self.id}) {str(self.modelo).upper()} {str(self.cor)} {self.ano}"

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
