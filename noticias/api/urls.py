from django.urls import path
from noticias.api.views import lista_articulos_crear_vista

urlpatterns = [
    path("articulos/", lista_articulos_crear_vista, name="lista-articulos")
]
