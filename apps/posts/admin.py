from django.contrib import admin
from .models import Categoria, Post


# Register your models here.(registrando la base de datos) = registramos los modelos de models.py

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    

admin.site.register(Categoria)