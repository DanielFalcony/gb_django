from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed successfully!')
    return HttpResponse('<h1>Добро пожаловать на мой первый сайт сделанный на Django!</h1>\n'
                        '<p>Пока что этот сайт довольно кривой, но надеюсь со временем это исправится =)</p>')


def about(request):
    logger.info('About page accessed successfully!')
    return HttpResponse('<h1>Пару слов обо мне:</h1>\n'
                        '<p>Меня зовут Соколовский Даниил, я вот что-то вроде пытаюсь'
                        'изучать Python :D</p>')
