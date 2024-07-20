from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tournaments', views.TournamentViewSet, basename='tournament')
router.register('player-tournament', views.PlayerTournamentViewSet, basename='player_tournament')

urlpatterns = router.urls
