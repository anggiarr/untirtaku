from django.shortcuts import render
from ft.models import Dosen, Staf, Mahasiswa
from ft.forms import FormDosen, FormStaf, FormMahasiswa

# Create your views here.
def indexft(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'dosen': dosen,
        'staf': staf,
        'mahasiswa': mahasiswa,
    }

    return render(request, 'bukaft.html')

def tambah_dosenft(request):
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
            return render(request, 'tambah-dosenft.html', konteks)
    else: 

        form = FormDosen()

        konteks = {
        'form' : form,
        }

    return render(request, 'tambah-dosenft.html', konteks)



def tambah_stafft(request):
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
            return render(request, 'tambah-stafft.html', konteks)
    else: 

        form1 = FormStaf()

        konteks = {
        'form' : form1,
        }

    return render(request, 'tambah-stafft.html', konteks)

def tambah_mahasiswaft(request):
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
            return render(request, 'tambah-mahasiswaft.html', konteks)
    else: 

        form2 = FormMahasiswa()

        konteks = {
        'form' : form2,
        }

    return render(request, 'tambah-mahasiswaft.html', konteks)


