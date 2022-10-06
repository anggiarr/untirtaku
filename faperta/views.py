from django.shortcuts import render

# Create your views here.
def indexfaperta(request):
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
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    

    konteks= {
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
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }

    return render(request, 'bukafaperta.html', konteks)