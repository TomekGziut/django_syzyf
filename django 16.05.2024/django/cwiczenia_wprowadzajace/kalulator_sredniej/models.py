from django.db import models

class Kalulator_sredniej(models.Model):
    nazwa_przedmiotu = models.CharField(max_length=255)
    lista_ocen = models.TextField()
    średnia_ocen = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nazwa_przedmiotu} - {self.lista_ocen} - {self.średnia_ocen}"

