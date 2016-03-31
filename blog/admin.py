from django.contrib import admin
from .models import Post

#Registra nuestr objet Pst en el administrador de Djang para poder consultar o actualizar informacion del o los posts
admin.site.register(Post)