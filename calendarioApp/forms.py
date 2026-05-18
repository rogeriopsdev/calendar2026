from django import forms
from django.db.models import fields
from calendarioApp.models import Tipo, Evento

class TipoForms(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'


class EventoForms(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['id_evento','data_evento',                  'nome_evento','id_tipo']
        id_evento =forms.IntegerField(label='Id_evento:')
        data_evento =forms.DateField(label='Data:')
        nome_evento =forms.CharField(label='Evento:')
        id_tipo =forms.CharField(label='Tipo:')
