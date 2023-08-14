from django.contrib import admin
from .models import Curso, Avaliacao


# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso_nome', 'nome', 'email', 'avaliacao_pontos', 'criacao', 'atualizacao', 'ativo')
