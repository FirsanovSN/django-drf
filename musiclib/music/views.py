from rest_framework import generics
from .models import Track
from .serializers import TrackSerializer
from .mixins import SearchOrderingFilterMixin

class TrackList(SearchOrderingFilterMixin, generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer