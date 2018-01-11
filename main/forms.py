from random import choices

from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Elo


class EloForm(forms.Form):
    Choices = (
        ('Sim', 'Sim'), ('Não', 'Não'))

    vitoria = forms.ChoiceField(choices=Choices, widget=forms.Select(attrs={'class':'select'}))
    pontos = forms.IntegerField(label='Pontos')

    def update_elo(form, usuario):
        vitoria = form.cleaned_data['vitoria']
        pontos = form.cleaned_data['pontos']

        if pontos + usuario.pontos >= 100:
            proximo_elo = Elo.objects.get(rank = usuario.elo.rank - 1)
            usuario.elo = proximo_elo
            usuario.pontos = (pontos + usuario.pontos) - 100
            usuario.save()
        else:
            pontos_totais = pontos + usuario.pontos
            usuario.pontos = pontos_totais
            usuario.save()




