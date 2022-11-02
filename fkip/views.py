from django.shortcuts import render, redirect
from fkip.models import Dosen, Staf, Mahasiswa
from fkip.forms import FormDosen, FormStaf, FormMahasiswa

# Create your views here.
def ubah_dosen(reuqest, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui")
            return redirect('ubah-dosen', id_dosen=id_dosen)
        
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form': form,
            'dosen': dosen,
        }

    return render(request, template, konteks)

def indexfkip(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'dosen': dosen,
        'staf': staf,
        'mahasiswa': mahasiswa,
    }

    return render(request, 'bukafkip.html')

def tambah_dosenfkip(request):
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
            return render(request, 'tambah-dosenfkip.html', konteks)
    else: 

        form = FormDosen()

        konteks = {
        'form' : form,
        }

    return render(request, 'tambah-dosenfkip.html', konteks)



def tambah_staffkip(request):
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
            return render(request, 'tambah-staffkip.html', konteks)
    else: 

        form1 = FormStaf()

        konteks = {
        'form' : form1,
        }

    return render(request, 'tambah-staffkip.html', konteks)

def tambah_mahasiswafkip(request):
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
            return render(request, 'tambah-mahasiswafkip.html', konteks)
    else: 

        form2 = FormMahasiswa()

        konteks = {
        'form' : form2,
        }

    return render(request, 'tambah-mahasiswafkip.html', konteks)


