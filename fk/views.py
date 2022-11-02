from django.shortcuts import render
from fk.models import Dosen, Staf, Mahasiswa
from fk.forms import FormDosen, FormStaf, FormMahasiswa

# Create your views here.
def indexfk(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'dosen': dosen,
        'staf': staf,
        'mahasiswa': mahasiswa,
    }

    return render(request, 'bukafk.html')

def tambah_dosenfk(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosenfk.html', konteks)
    else: 

        form = FormDosen()

        konteks = {
        'form' : form,
        }

    return render(request, 'tambah-dosenfk.html', konteks)



def tambah_staffk(request):
    if request.POST:
        form1 = FormStaf(request.POST)
        if form1.is_valid():
            form1.save()
            form1 = FormStaf()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form1,
                'pesan': pesan,
            }
            return render(request, 'tambah-staffk.html', konteks)
    else: 

        form1 = FormStaf()

        konteks = {
        'form' : form1,
        }

    return render(request, 'tambah-staffk.html', konteks)

def tambah_mahasiswafk(request):
    if request.POST:
        form2 = FormMahasiswa(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form2,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswafk.html', konteks)
    else: 

        form2 = FormMahasiswa()

        konteks = {
        'form' : form2,
        }

    return render(request, 'tambah-mahasiswafk.html', konteks)

