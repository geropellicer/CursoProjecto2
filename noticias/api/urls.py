from django.urls import path
from noticias.api.views import (detalles_articuloAPIView,
                                lista_articulosAPIView)

urlpatterns = [
    path("articulos/", lista_articulosAPIView.as_view(), name="lista-articulos"),
    path("articulos/<int:pk>", detalles_articuloAPIView.as_view(), name="detalles-articulo"),
]
