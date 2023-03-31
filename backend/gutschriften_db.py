from django.db import models
from django_uuid_upload import upload_to_uuid

from .firms_db import Firm
from .own_firms_db import OwnFirm


# class Avis(models.Model):
#     firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True)
#     avis_nr = models.CharField(max_length=50, unique=True)
#
#     class Meta:
#         verbose_name_plural = 'Avises'
#
#     def __str__(self):
#         return self.avis_nr


class Gutschrift(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateField()
    start = models.DateField()
    end = models.DateField()
    document_nr = models.CharField(max_length=200, unique=True)
    gross_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    taxes = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    open_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    completely_paid = models.BooleanField(default=False)
    completely_paid_date = models.DateField(blank=True, null=True)
    avis = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to=upload_to_uuid('Gutschriften'), blank=True, null=True, max_length=800)

    class Meta:
        verbose_name_plural = 'Gutschrifts'

    def __str__(self):
        return str(self.creation_date)


class GutschriftPayment(models.Model):
    gutschrift = models.ForeignKey(Gutschrift, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Gutschrift Payments'

    def __str__(self):
        return f'{self.id}'



