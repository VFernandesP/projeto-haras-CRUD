from django.contrib import admin
from .models import Cavalo
from django.utils.html import format_html       

@admin.register(Cavalo)
class CavaloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'sexo', 'valor', 'ativo', 'foto_preview')
    
    list_filter = ('sexo', 'ativo', 'raca')  
    
    search_fields = ('nome', 'raca', 'registro')
    
    readonly_fields = ('foto_preview',)
    
    def foto_preview(self, obj):
        if obj.foto:
            return f'<img src="{obj.foto.url}" width="50" height="50" style="border-radius:8px;" />'
        return "Sem foto"
    foto_preview.allow_tags = True  
    foto_preview.short_description = 'Foto'