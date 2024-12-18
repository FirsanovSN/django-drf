from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=200)  # Название трека
    artist = models.CharField(max_length=200)  # Исполнитель
    album = models.CharField(max_length=200, blank=True, null=True)  # Альбом
    genre = models.CharField(max_length=100, blank=True, null=True)  # Жанр
    duration = models.IntegerField()  # Длительность в секундах
    release_date = models.DateField(blank=True, null=True)  # Дата выпуска

    def __str__(self):
        return f"{self.title} - {self.artist}"