
from django.contrib import admin
from django.urls import path
from fkip.views import *
from faperta.views import *
from feb.views import *
from fh.views import *
from fisip.views import *
from fk.views import *
from ft.views import indexft, tambah_dosenft, tambah_mahasiswaft, tambah_stafft
from pascasarjana.views import indexpascasarjana, tambah_dosenpascasarjana, tambah_mahasiswapascasarjana, tambah_stafpascasarjana
from profil.views import indexprofil
from aboutuntirta.views import indexabout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', indexfkip),
    path('faperta/', indexfaperta),
    path('feb/', indexfeb),
    path('fh/', indexfh),
    path('fisip/', indexfisip),
    path('fk/', indexfk),
    path('ft/', indexft),
    path('pascasarjana/', indexpascasarjana),
    path('profil/', indexprofil), 
    path('aboutuntirta/', indexabout), 
    path('tambah-dosenfaperta/', tambah_dosenfaperta, name="tambah_dosenfaperta"),
    path('tambah-staffaperta/', tambah_staffaperta, name="tambah_staffaperta"),
    path('tambah-mahasiswafaperta/', tambah_mahasiswafaperta, name="tambah_mahasiswafaperta"),
    path('tambah-dosenfeb/', tambah_dosenfeb, name="tambah_dosenfeb"),
    path('tambah-staffeb/', tambah_staffeb, name="tambah_staffeb"),
    path('tambah-mahasiswafeb/', tambah_mahasiswafeb, name="tambah_mahasiswafeb"),
    path('tambah-dosenfh/', tambah_dosenfh, name="tambah_dosenfh"),
    path('tambah-staffh/', tambah_staffh, name="tambah_staffh"),
    path('tambah-mahasiswafh/', tambah_mahasiswafh,  name="tambah_mahasiswafh"),
    path('tambah-dosenfisip/', tambah_dosenfisip,  name="tambah_dosenfisip"),
    path('tambah-staffisip/', tambah_staffisip,  name="tambah_staffisip"),
    path('tambah-mahasiswafisip/', tambah_mahasiswafisip,  name="tambah_mahasiswafisip"),
    path('tambah-dosenfk/', tambah_dosenfk,  name="tambah_dosenfk"),
    path('tambah-staffk/', tambah_staffk,  name="tambah_staffk"),
    path('tambah-mahasiswafk/', tambah_mahasiswafk,  name="tambah_mahasiswafk"),
    path('tambah-dosenfkip/', tambah_dosenfkip, name="tambah_dosenfkip"),
    path('tambah-staffkip/', tambah_staffkip, name="tambah_staffkip"),
    path('tambah-mahasiswafkip/', tambah_mahasiswafkip, name="tambah_mahasiswafkip"),
    path('tambah-dosenft/', tambah_dosenft,  name="tambah_dosenft"),
    path('tambah-stafft/', tambah_stafft,  name="tambah_stafft"),
    path('tambah-mahasiswaft/', tambah_mahasiswaft,  name="tambah_mahasiswaft"),
    path('tambah-dosenpascasarjana/', tambah_dosenpascasarjana,  name="tambah_dosenpascasarjana"),
    path('tambah-stafpascasarjana/', tambah_stafpascasarjana,  name="tambah_stafpascasarjana"),
    path('tambah-mahasiswapascasarjana/', tambah_mahasiswapascasarjana,  name="tambah_mahasiswapascasarjana"),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('staf/ubah/<int:id_staf>', ubah_staf, name='ubah_staf'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    






    

    

]
