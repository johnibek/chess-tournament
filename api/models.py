from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class Tournament(models.Model):
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateTimeField(validators=[MinValueValidator(timezone.now)], default=timezone.now)
    end_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    rounds = models.SmallIntegerField(validators=[MinValueValidator(1)])

    def clean(self):
        super().clean()
        if self.end_date < self.start_date:
            raise ValidationError("end date cannot be earlier than start date")


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class PLayerTournament(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.username} participating in {self.tournament.name}"


