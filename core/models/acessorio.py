from django.db import models


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Acessório'

    def __str__(self):
        return f"({self.id}) {self.descricao}"
