from random import choices

from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Elo


class EloForm(forms.Form):
    Choices = (
        ('Sim', 'Sim'), ('Não', 'Não'))

    vitoria = forms.ChoiceField(label='Você ganhou o jogo?', choices=Choices, widget=forms.Select(attrs={'class':'select'}))
    pontos = forms.IntegerField(label='Pontos de não-rage')

    def update_elo(form, usuario):
        vitoria = form.cleaned_data['vitoria']
        pontos = form.cleaned_data['pontos']

        print(vitoria)

        if pontos + usuario.pontos >= 100:
            proximo_elo = Elo.objects.get(rank = usuario.elo.rank - 1)
            usuario.elo = proximo_elo
            usuario.pontos = (pontos + usuario.pontos) - 100
            if vitoria == 'Sim':
                usuario.partidas_ganhas = usuario.partidas_ganhas + 1
            else:
                usuario.partidas_perdidas = usuario.partidas_perdidas + 1
            usuario.partidas_jogadas = usuario.partidas_jogadas + 1
            usuario.save()
        else:
            pontos_totais = pontos + usuario.pontos
            usuario.pontos = pontos_totais
            if vitoria == 'Sim':
                usuario.partidas_ganhas = usuario.partidas_ganhas + 1
            else:
                usuario.partidas_perdidas = usuario.partidas_perdidas + 1
            usuario.partidas_jogadas = usuario.partidas_jogadas + 1
            usuario.save()

