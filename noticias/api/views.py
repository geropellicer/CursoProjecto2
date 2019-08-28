from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from noticias.models import Articulo
from noticias.api.serializers import ArticuloSerializer

@api_view(['GET', 'POST'])
def lista_articulos_crear_vista(request):
    
    if request.method == 'GET':
        articulos = Articulo.objects.filter(activo=True)
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticuloSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalles_articulo_crear_vista(request, pk):
    try:
        articulo = Articulo.objects.get(pk=pk)
    except Articulo.DoesNotExist:
        return Response({
            "error": {
                'codigo': 404,
                'mensaje': 'Articulo no encontrado'
            }}, status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)
    
    elif(request.method == 'PUT'):
        serializer = ArticuloSerializer(articulo, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)