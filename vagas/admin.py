from django.contrib import admin
from.models import Vaga
# Register your models here.

class listando_vagas(admin.ModelAdmin):
    list_display = ('id', 'nome_vaga', 'faixa_salarial', 'escolaridade')
    list_display_links = ('id', 'nome_vaga')

    
admin.site.register(Vaga, listando_vagas)
