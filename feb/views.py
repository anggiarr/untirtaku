from django.shortcuts import render
from feb.models import Dosen, Staf, Mahasiswa
from feb.forms import FormDosen, FormStaf, FormMahasiswa
from django.contrib import messages 

# Create your views here.
def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui")
            return redirect('ubah_dosen', id_dosen=id_dosen)
        
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form': form,
            'dosen': dosen,
        }

    return render(request, template, konteks)


def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
        
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form': form,
            'mahasiswa': mahasiswa,
        }

    return render(request, template, konteks)


def ubah_staf(request, id_staf):
    staf = Staf.objects.get(id=id_staf)
    template = 'ubah-staf.html'
    if request.POST:
        form = FormStaf(request.POST, instance=staf)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui")
            return redirect('ubah_staf', id_mahasiswa=id_staf)
        
    else:
        form = FormStaf(instance=staf)
        konteks = {
            'form': form,
            'staf': staf,
        }

    return render(request, template, konteks)



def indexfeb(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'dosen': dosen,
        'staf': staf,
        'mahasiswa': mahasiswa,
    }

    return render(request, 'bukafeb.html')

def tambah_dosenfeb(request):
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
            return render(request, 'tambah-dosenfeb.html', konteks)
    else: 

        form = FormDosen()

        konteks = {
        'form' : form,
        }

    return render(request, 'tambah-dosenfeb.html', konteks)



def tambah_staffeb(request):
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
            return render(request, 'tambah-staffeb.html', konteks)
    else: 

        form1 = FormStaf()

        konteks = {
        'form' : form1,
        }

    return render(request, 'tambah-staffeb.html', konteks)

def tambah_mahasiswafeb(request):
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
            return render(request, 'tambah-mahasiswafeb.html', konteks)
    else: 

        form2 = FormMahasiswa()

        konteks = {
        'form' : form2,
        }

    return render(request, 'tambah-mahasiswafeb.html', konteks)

