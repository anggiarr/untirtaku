from django.shortcuts import render, redirect
from faperta.models import Dosen, Staf, Mahasiswa
from faperta.forms import FormDosen, FormStaf, FormMahasiswa
from django.contrib import messages 

# Create your views here.
def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()

    messages.success(request, "Data Berhasil dihapus!")

    return redirect('bukafaperta')


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


def indexfaperta(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    tentang = "Program Studi di Fakultas Pertanian"
    prodisatu = "Agribisnis"
    penjelasanprodisatu = "Pada Tahun 2009 Program Studi Sosial Ekonomi Pertanian berubah menjadi Jurusan/Program Studi Agribisnis, dengan Keputusan Rektor No. 181/H43/KR/SK/2009 dan diakreditasi kembali pada tahun 2012 dengan akreditasi B berdasarkan SK BAN PT Nomor: 024/BAN-PT/Ak-XV/S1/VIII/2012."
    prodidua = "Agroekoteknologi"
    penjelasanprodidua = "Jurusan agroekoteknologi merupakan suatu upaya turut sertanya Faperta Untirta dalam menunjang pembangunan nasional dan daerah terutama dalam pengembangan pemanfaatan dan pengelolaan sumber daya alam (SDA) dan sumber daya manusia (SDM) khususnya di sektor pertanian. Upaya tersebut diwujudkan dalam bentuk kerjasama dengan instansi pemerintah, swasta, dan Perguruan Tinggi. Kondisi tersebut diharapkan dapat memberikan peluang bagi lulusan jurusan agroekoteknologi untuk berkiprah di instansi pemerintah, swasta, maupun menjadi wiraswasta"
    proditiga = "Ilmu Perikanan"
    penjelasanproditiga = "Prodi Perikanan merupakan salah satu Prodi yang berada di lingkungan Fakultas Pertanian (Faperta), Universitas Sultan Ageng Tirtayasa (Untirta). Pendirian Prodi Perikanan mulai direncanakan sejak tahun 2003 sebagai upaya untuk memenuhi permintaan sumberdaya manusia di sektor perikanan baik instansi pemerintah maupun swasta. Selain itu, hal lain yang mendasarinya adalah potensi kelautan dan perikanan Provinsi Banten yang prospektif untuk dikembangkan."
    prodiempat = "Teknologi Pangan"
    penjelasanprodiempat = "Untuk mendukung pengembangan Untirta sebagai Center of Excellence for Food Security, maka pada bulan Maret 2017 Fakultas Pertanian Untirta mengajukan  pendirian PS Teknologi Pangan dan mendapatkan izin operasional pada tanggal 10 Juli 2017 berdasarkan SK Menteri Riset, Teknologi, dan Pendidikan Tinggi RI Nomor 402/KPT/I/2017 tentang Izin Pembukaan Program Studi Teknologi Pangan Program Sarjana pada Universitas Sultan Ageng Tirtayasa."
    lokasi = "Lokasi Kampus"
    alamat = "Fakultas Pertanian berlokasi di Jl. Raya Palka Sindangsari, Kec. Pabuaran, Kabupaten Serang, Banten"

    konteks= {
        'dosen': dosen,
        'staf': staf,
        'mahasiswa': mahasiswa,
        'judul' : tentang,
        'jurusan1' : prodisatu,
        'penjelasanprodisatu' : penjelasanprodisatu,  
        'jurusan2' : prodidua,
        'penjelasanprodidua' : penjelasanprodidua,
        'jurusan3' : proditiga,
        'penjelasanproditiga' : penjelasanproditiga,
        'jurusan4' : prodiempat,
        'penjelasanprodiempat' : penjelasanprodiempat,
        'lokasi' : lokasi,
        'alamat' : alamat,
    }

    return render(request, 'bukafaperta.html', konteks)

def tambah_dosenfaperta(request):
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
            return render(request, 'tambah-dosenfaperta.html', konteks)
    else: 

        form = FormDosen()

        konteks = {
        'form' : form,
        }

    return render(request, 'tambah-dosenfaperta.html', konteks)



def tambah_staffaperta(request):
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
            return render(request, 'tambah-staffaperta.html', konteks)
    else: 

        form1 = FormStaf()

        konteks = {
        'form' : form1,
        }

    return render(request, 'tambah-staffaperta.html', konteks)

def tambah_mahasiswafaperta(request):
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
            return render(request, 'tambah-mahasiswafaperta.html', konteks)
    else: 

        form2 = FormMahasiswa()

        konteks = {
        'form' : form2,
        }

    return render(request, 'tambah-mahasiswafaperta.html', konteks)