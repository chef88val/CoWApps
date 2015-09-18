from django.contrib import admin

from .models import Entrada
# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
    fields = ['user', 'description']




admin.site.register(Entrada)