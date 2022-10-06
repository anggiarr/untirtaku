from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def indexft(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    

    konteks= {
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'bukaft.html', konteks)