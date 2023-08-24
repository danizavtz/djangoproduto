from django.db import models

class Produtos(models.Model):
    compra = models.DecimalField(db_column='compra', max_digits=15, decimal_places=5)  # Field name made lowercase.
    venda = models.DecimalField(db_column='venda', max_digits=15, decimal_places=5)  # Field name made lowercase.
    cotacaocompra = models.DecimalField(db_column='cotacaoCompra', max_digits=15, decimal_places=5)  # Field name made lowercase.
    cotacaovenda = models.DecimalField(db_column='cotacaoVenda', max_digits=15, decimal_places=5)  # Field name made lowercase.
    datahoracotacao = models.DateTimeField(db_column='dataHoraCotacao')  # Field name made lowercase.
    tipo = models.CharField(db_column='tipo', max_length=30)  # Field name made lowercase.

    def __str__(self):
        return f'venda: {self.cotacaovenda} | data: {self.datahoracotacao}'

    class Meta:
        managed = True
        db_table = 'produtos'
