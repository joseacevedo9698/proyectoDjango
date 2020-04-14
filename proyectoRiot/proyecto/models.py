from django.db import models
from django.utils import timezone

class Summoner(models.Model):
    summon_name = models.CharField(max_length=100)
    server      = models.CharField(max_length=10)
    profile = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.summon_name