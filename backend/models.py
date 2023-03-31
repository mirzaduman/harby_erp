from django.db import models

# Create your models here.


class Tests(models.Model):
    file_test = models.FileField(upload_to='test/', blank=True, null=True)
    string_test = models.CharField(max_length=5000, blank=True, null=True)
    # integer_test = models.IntegerField(blank=True, null=True)