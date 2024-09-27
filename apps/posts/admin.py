from django.contrib import admin
from .models import Categoria, Post


# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    

admin.site.register(Categoria)