from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta película")
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    date_release = models.DateField(null=True, blank=True, help_text="Fecha de estreno")
    synopsis = models.TextField(max_length=500, help_text="Sinopsis de la película")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.last_name)])

    def __str__(self):
        return '%s (%s)' % (self.last_name, self.first_name)
