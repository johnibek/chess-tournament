from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # USER_ROLES = (
    #     ('player', 'player'),
    #     ('admin', 'admin')
    # )

    # user_role = models.CharField(max_length=50, choices=USER_ROLES, default='player')

    # def save(self, *args, **kwargs):
    #     if self.is_superuser:
    #         self.user_role = 'admin'

    #     super().save(*args, **kwargs)
    age = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

