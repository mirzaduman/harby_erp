import uuid

from django.db import models
from django.contrib.auth.models import User
from .own_firms_db import OwnFirm


class Colour(models.Model):
    name = models.CharField(max_length=50)
    colour_hex = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Colours'

    def __str__(self):
        return self.name


class HarbyAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    own_firms = models.ManyToManyField(OwnFirm, blank=True)
    user_hash = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name_plural = 'Harby Admins'

    def __str__(self):
        return self.user.username


class Log(models.Model):
    admin = models.ForeignKey(HarbyAdmin, on_delete=models.SET_NULL, null=True)
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    log_input = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Logs'

    def __str__(self):
        return self.admin.user.username
