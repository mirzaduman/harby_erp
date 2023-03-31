import uuid
from django_uuid_upload import upload_to_uuid
from django.db import models
from .firms_db import Firm
from .own_firms_db import OwnFirm
from random import randint


class Product(models.Model):
    position = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=16)
    unit = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=16, blank=True, null=True)
    sum = models.DecimalField(decimal_places=2, max_digits=16)

    def __str__(self):
        return self.description


class Bill(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True)
    bill_nr = models.CharField(max_length=200)
    bill_nr_int = models.PositiveIntegerField(default=0)
    customer_tax_nr = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    creation_date = models.DateField()
    has_to_be_paid_date_start = models.DateField(blank=True, null=True)
    has_to_be_paid_date_end = models.DateField(blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    sum = models.DecimalField(decimal_places=2, max_digits=16, null=True)
    taxes = models.DecimalField(default=19, decimal_places=2, max_digits=16)
    end_sum = models.DecimalField(decimal_places=2, max_digits=16, null=True)
    pdf = models.FileField(upload_to='Rechnungen', blank=True, null=True, max_length=800)
