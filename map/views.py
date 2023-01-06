from django.shortcuts import render, redirect
import folium
from map.models import *
from map.forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def tpi(request):
    #Create Map Object
    m = folium.Map(location=[-6.1734372999771185, 106.8270224802792], zoom_start=12)
    folium.Marker([-6.097653724131664, 106.93950855436613], tooltip='Click for more',
                    popup='TPI Cilincing').add_to(m)
    folium.Marker([-6.102197866678709, 106.9201237562112], tooltip='Click for more',
                    popup='TPI Kali Baru').add_to(m)
    folium.Marker([-6.098960220151633, 106.77435755047361], tooltip='Click for more',
                    popup='TPI Muara Angke').add_to(m)
    folium.Marker([-6.0825737541618405, 106.72491907886462], tooltip='Click for more',
                    popup='TPI Kamal').add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    ikan = TPI.objects.all()
    judul = "TPI Jakarta | Home"
    konteks = {
        "title" : judul,
        'm' : m,
        'ikan' : ikan,
    }
    return render (request, 'tpi.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_tpi(request):
    if request.POST:
        form = FormTPI(request.POST)
        if form.is_valid():
            form.save()
            form = FormTPI()
            judul = "TPI Jakarta | Add Data"
            pesan = "Data berhasil ditambahkan!"
            konteks = {
                "title" : judul,
                "form" : form,
                "pesan" : pesan,
            }
            return render (request, 'tambah_tpi.html', konteks)
    else:
        form = FormTPI()
        judul = "TPI Jakarta | Add Data"
        konteks = {
            "title" : judul,
            "form" : form,
        }
    return render (request, 'tambah_tpi.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def update_tpi(request, id_fish):
    fish = TPI.objects.get(id = id_fish)
    judul = "TPI Jakarta | Update Data"
    template = "update_tpi.html"
    
    if request.POST:
        form = FormTPI(request.POST, instance=fish)
        if form.is_valid():
            form.save()
            pesan = "Data berhasil diubah!"
            konteks = {
                "title" : judul,
                "form" : form,
                "pesan" : pesan,
                'fish' : fish,
            }
            return render (request, template, konteks)
    else:
        form = FormTPI(instance=fish)
        konteks = {
            "title" : judul,
            "form" : form,
            'fish' : fish,
        }
    return render (request, template, konteks)

def delete_tpi(request, id_fish):
    fish = TPI.objects.get(id = id_fish)
    fish.delete()
    
    return redirect ("/tpi/")

@login_required(login_url=settings.LOGIN_URL)
def lihat_detail(request, id_fish):
    fish = TPI.objects.get(id = id_fish)
    template = "lihat_detail.html"
    judul = "TPI Jakarta | Detail"
    konteks = {
        'fish' : fish,
        'title' : judul,
    }
    return render (request, template, konteks)