from django.db import models
from django_uuid_upload import upload_to_uuid

from backend.own_firms_db import OwnFirm


class Truck(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    plate = models.CharField(max_length=50, unique=True)
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    PAYMENT_METHODS = [
        ('Barzahlung', 'Barzahlung'), ('Ratenzahlung', 'Ratenzahlung')
    ]
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=200, blank=True, null=True)
    paid_day = models.DateField(blank=True, null=True)
    paid_status = models.BooleanField(blank=True, null=True)
    total_installment_months = models.PositiveIntegerField(default=0, blank=True, null=True)
    installment_monthly_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    installment_start_date = models.DateField(blank=True, null=True)
    installment_end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Trucks'

    def __str__(self):
        return self.plate


class TruckDocument(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_to_uuid('LKW_Dokumente'), blank=True, null=True, max_length=800)
    expiry_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Truck Documents'

    def __str__(self):
        return self.name



