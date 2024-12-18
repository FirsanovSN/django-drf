from django.contrib import admin
from .models import Artist, Track

# Регистрация модели Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')  # Отображаемые поля в списке исполнителей
    search_fields = ('name',)  # Поле для поиска по имени исполнителя

# Регистрация модели Track
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'genre', 'duration', 'release_date')  # Отображаемые поля в списке треков
    list_filter = ('artist', 'genre', 'release_date')  # Фильтры для поиска
    search_fields = ('title', 'artist__name')  # Поле для поиска по названию трека и имени исполнителя
    list_editable = ('artist',)  # Позволяет редактировать поле "artist" в списке