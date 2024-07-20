from rest_framework import serializers
from .models import Tournament, PLayerTournament
from users.serializers import CustomUserSerializer


class PLayerSerializer(serializers.ModelSerializer):
    player = CustomUserSerializer(read_only=True)
    player_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PLayerTournament
        fields = ['id', 'player', 'player_id']

class TournamentSerializer(serializers.ModelSerializer):
    players = PLayerSerializer(source='playertournament_set', many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = ['id', 'name', 'start_date', 'end_date', 'description', 'rounds', 'players']


class PlayerTournamentSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    player_id = serializers.IntegerField(write_only=True)
    tournament_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PLayerTournament
        fields = ['id', 'tournament', 'player_id', 'tournament_id']

