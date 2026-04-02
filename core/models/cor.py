from django.db import models


class Cor(models.Model):
    nome = models.CharField(max_length=40)

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return f"({self.id}) {self.nome}"
