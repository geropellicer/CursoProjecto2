from django.urls import path
from noticias.api.views import (lista_articulos_crear_vista,
                                detalles_articulo_crear_vista)

urlpatterns = [
    path("articulos/", lista_articulos_crear_vista, name="lista-articulos"),
    path("articulos/<int:pk>", detalles_articulo_crear_vista, name="detalles-articulo"),
]
