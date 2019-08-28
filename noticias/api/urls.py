from django.urls import path
from noticias.api.views import (detalles_articuloAPIView,
                                lista_articulosAPIView,
                                detalles_escritorAPIView,
                                lista_escritoresAPIView)

urlpatterns = [
    path("articulos/", lista_articulosAPIView.as_view(), name="lista-articulos"),
    path("articulos/<int:pk>", detalles_articuloAPIView.as_view(), name="detalles-articulo"),
    path("escritores/", lista_escritoresAPIView.as_view(), name="lista-escritores"),
    path("escritores/<int:pk>", detalles_escritorAPIView.as_view(), name="detalles-escritor"),
]
