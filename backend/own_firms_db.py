from django.db import models


class OwnFirm(models.Model):
    name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='firmen_logos/', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    mail = models.CharField(max_length=200, blank=True, null=True)
    chairman = models.CharField(max_length=200, blank=True, null=True)
    company_place = models.CharField(max_length=200, blank=True, null=True)
    register_court = models.CharField(max_length=200, blank=True, null=True)
    tax_nr = models.CharField(max_length=200, blank=True, null=True)
    ustid = models.CharField(max_length=200, blank=True, null=True)
    contact_name = models.CharField(max_length=200, blank=True, null=True)
    contact_phone = models.CharField(max_length=200, blank=True, null=True)
    contact_fax = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    bank_iban = models.CharField(max_length=200, blank=True, null=True)
    bank_bic = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Own Firms"

    def __str__(self):
        return self.name
