from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)  # Имя исполнителя
    bio = models.TextField(blank=True, null=True)  # Биография исполнителя

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=200)  # Название трека
    artist = models.ForeignKey(Artist, related_name='tracks', on_delete=models.CASCADE)  # Исполнитель
    album = models.CharField(max_length=200, blank=True, null=True)  # Альбом
    genre = models.CharField(max_length=100, blank=True, null=True)  # Жанр
    duration = models.IntegerField()  # Длительность в секундах
    release_date = models.DateField(blank=True, null=True)  # Дата выпуска

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
