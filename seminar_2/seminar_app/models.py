from django.db import models
from django.db.models import Manager


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    object = Manager()

    def __str__(self):
        return f'Результат броска: {self.result}, Время броска: {self.played}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.object.all()[:n]


class Authors(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name}'
