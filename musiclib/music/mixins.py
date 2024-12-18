from rest_framework import filters

class SearchOrderingFilterMixin:
    """
    Миксин для добавления поиска, фильтрации и сортировки.
    """
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'artist', 'album', 'genre']  # Поля для поиска
    ordering_fields = ['title', 'artist', 'release_date']  # Поля для сортировки