from django.contrib import admin
from .models import Tournament, PLayerTournament

admin.site.register([Tournament, PLayerTournament])