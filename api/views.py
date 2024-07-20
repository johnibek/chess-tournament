from rest_framework import generics, viewsets
from .models import Tournament, PLayerTournament
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import TournamentSerializer, PlayerTournamentSerializer


# Tournament
class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.all()
    permission_classes = [IsAdminUser]


class PlayerTournamentViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerTournamentSerializer
    queryset = PLayerTournament.objects.all()
    permission_classes = [IsAdminUser]
