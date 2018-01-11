# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from .models import Elo, PontosUsuario
from .forms import EloForm


def index(request):
    elo_usuario = PontosUsuario.objects.get(id=1)
    success = False
    form = EloForm(request.POST or None)
    if form.is_valid():
        success = True
        EloForm.update_elo(form, elo_usuario)
    context = {
        'sucess':success,
        'form': form,
        'eloUsuario': elo_usuario
    }
    return render(request, template_name='index.html', context=context)