from django.urls import path
from .views import TrackList, TrackDetail, CustomAuthToken, protected_view, custom_login, ProtectedAPIView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('tracks/', TrackList.as_view(), name='track-list'),  # Список треков
    path('tracks/<int:pk>/', TrackDetail.as_view(), name='track-detail'),  # Детали трека

    path('protected/', protected_view, name='protected'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', custom_login, name='login'),
    path('api/protected/', ProtectedAPIView.as_view(), name='protected-api'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Маршрут для выхода


]