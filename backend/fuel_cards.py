from django.db import models
from .workers_db import Worker
from .own_firms_db import OwnFirm


class FuelcardFirm(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Fuelcard Firms"

    def __str__(self):
        return self.name


class Fuelcard(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    # firm_name = models.CharField(max_length=50, blank=True, null=True)
    firm = models.ForeignKey(FuelcardFirm, on_delete=models.SET_NULL, null=True)
    card_nr = models.CharField(max_length=50, unique=True)
    card_is_at = models.ForeignKey(Worker, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Fuelcards"

    def __str__(self):
        return self.card_nr


class FuelcardActivities(models.Model):
    got_date = models.DateField()
    gave_back_date = models.DateField(blank=True, null=True)
    fuelcard = models.ForeignKey(Fuelcard, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Fuelcard Activities"

    def __str__(self):
        return f'{self.driver} - {self.got_date}'
