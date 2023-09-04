from random import randint

from django.http import HttpResponse
from django.shortcuts import render

from seminar_app.models import GameModel, Authors


def index(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_game(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(result) for result in last]
    return HttpResponse(last_str)


def author(request):
    result = Authors.objects.all()