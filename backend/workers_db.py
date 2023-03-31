import datetime

from django.db import models
from django_uuid_upload import upload_to_uuid

from .own_firms_db import OwnFirm


class Position(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name


class Worker(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    worker_id = models.CharField(max_length=200, unique=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    daily_expense = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    is_driver = models.BooleanField(default=False)
    holidays = models.PositiveIntegerField(default=25)
    start_date = models.DateField()
    is_working = models.BooleanField(default=True)
    has_quit = models.BooleanField(default=False)
    quit_date = models.DateField(blank=True, null=True)
    remaining_debts = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    paid_debts = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Workers"

    def __str__(self):
        return self.name


class DebtPayment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Debts"


class WorkerActivity(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    activity = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Worker Activities"

    def __str__(self):
        return self.activity[:20]


class HolidayAccount(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    used_holiday_days = models.IntegerField(blank=True, null=True)
    remaining_holiday_days = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=4)


class OffdayTag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    colour = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Offday Tags"

    def __str__(self):
        return self.name


class Offday(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    tag = models.ForeignKey(OffdayTag, on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Offdays"

    def __str__(self):
        return f'{self.worker.name} : {self.date}'


class WorkerDocument(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_to_uuid('Mitarbeiter_Dokumente'), blank=True, null=True, max_length=800)
    expiry_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Worker Documents"

    def __str__(self):
        return self.name


class WorkTime(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField(default=datetime.time(0, 0, 0))
    pause = models.TimeField(default=datetime.time(0, 0, 0))
    end = models.TimeField(default=datetime.time(0, 0, 0))
    duration = models.TimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Work Times'

    def __str__(self):
        return f'{self.worker.name}  {self.date}'

