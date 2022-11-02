from django.db import models

# Create your models here.
class Dosen(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField()

def _str_(self):
    return self.nama

class Staf(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    alamat = models.TextField()

def _str_(self):
    return self.nama

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField()

def _str_(self):
    return self.nama