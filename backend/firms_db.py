from django.db import models
from .own_firms_db import OwnFirm


class Firm(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    vat = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Firms"

    def __str__(self):
        return self.name



