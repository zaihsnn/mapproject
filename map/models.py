from django.db import models

# Create your models here.

class TPI(models.Model):
    nomer = models.IntegerField(null=True)
    nama = models.CharField(max_length=500)
    alamat = models.CharField(max_length=500)
    jam_buka = models.CharField(max_length=500)
    gambar = models.CharField(max_length=500)

    def __str__(self):
        return self.nama

