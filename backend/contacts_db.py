from django.db import models
from .own_firms_db import OwnFirm


class ContactTag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    colour = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    own_firm = models.ForeignKey(OwnFirm, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    firm = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    mail = models.EmailField(max_length=200, blank=True, null=True)
    tag = models.ForeignKey(ContactTag, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Meeting(models.Model):
    meetings_notes = models.TextField(blank=True, null=True)
    meetings_date = models.DateField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Meetings"

    def __str__(self):
        return f'{self.meetings_date} - {self.contact.name}'