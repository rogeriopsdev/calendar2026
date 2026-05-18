from django.db import models

# Create your models here.
class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_tipo


class Evento(models.Model):
    id_evento = models.AutoField(primary_key= True)
    data_evento = models.CharField(max_length=255, null=True)
    nome_evento = models.CharField(max_length=255, null=False)
    id_tipo =models.ForeignKey(Tipo,models.DO_NOTHING,
                               db_column='id_tipo', null=False)

    def __str__(self):
        return self.nome_evento

