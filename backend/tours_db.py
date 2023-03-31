from django.db import models
from .workers_db import Worker
from .firms_db import Firm
from .trucks_db import Truck
from .own_firms_db import OwnFirm


class DailyNote(models.Model):
    note = models.CharField(max_length=4000)
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Daily Notes"

    def __str__(self):
        return f'{self.date} - - - {self.note}'


class TourStatus(models.Model):
    name = models.CharField(max_length=200, unique=True)
    colour = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tour Status"

    def __str__(self):
        return self.name


class Tour(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    roller_nr = models.CharField(max_length=400, unique=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True)
    general_notes = models.CharField(max_length=1000, blank=True, null=True)
    default_truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, blank=True, null=True)
    default_driver = models.ForeignKey(Worker, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tours"

    def __str__(self):
        return self.roller_nr


class TourDay(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.ForeignKey(TourStatus, on_delete=models.SET_NULL, null=True)
    drivers = models.ManyToManyField(Worker)
    vehicle = models.ForeignKey(Truck, blank=True, null=True, on_delete=models.SET_NULL)
    daily_note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tour Days"

    def __str__(self):
        return str(self.tour.firm) + str(self.date)


