from django.contrib import admin
from .models import *


class tpiadmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'jam_buka', 'gambar']
    search_fields = ['nama']

# Register your models here.
admin.site.register (TPI, tpiadmin)