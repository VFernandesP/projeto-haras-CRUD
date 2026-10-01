from django.contrib import admin
from .models import Cavalo, Proprietario, Veterinario, Atendimento
from django.utils.html import format_html


@admin.register(Cavalo)
class CavaloAdmin(admin.ModelAdmin):
    list_display = ("nome", "raca", "sexo", "valor", "ativo", "foto_preview")

    list_filter = ("sexo", "ativo", "raca")

    search_fields = ("nome", "raca", "registro")

    readonly_fields = ("foto_preview",)

    def foto_preview(self, obj):
        if obj.foto:
            return f'<img src="{obj.foto.url}" width="50" height="50" style="border-radius:8px;" />'
        return "Sem foto"

    foto_preview.allow_tags = True
    foto_preview.short_description = "Foto"


@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "email")
    search_fields = ("nome", "telefone", "email")


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "crmv", "telefone", "email")
    search_fields = ("nome", "crmv", "telefone", "email")


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ("cavalo", "veterinario", "data", "descricao")
    list_filter = ("data", "veterinario")
    search_fields = ("cavalo__nome", "veterinario__nome", "descricao")
