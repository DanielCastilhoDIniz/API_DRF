from django.contrib import admin

from .models import Curso, Avaliacao

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'created', 'updated')
    search_fields = ('id', 'title', 'url')
    list_filter = ('id', 'title')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'created', 'updated')
    search_fields = ('id', 'curso', 'nome', 'email', 'comentario')
    list_filter = ('id', 'curso', 'nome', 'email')
    raw_id_fields = ['curso']
    readonly_fields = ['created', 'updated']
    list_per_page = 20
    ordering = ['id']
    autocomplete_fields = ['curso']
    list_editable = ['avaliacao']
    



