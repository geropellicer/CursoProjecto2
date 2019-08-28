from rest_framework import status
from rest_framework.decorators import APIView #, api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from noticias.models import Articulo
from noticias.api.serializers import ArticuloSerializer

# @api_view(['GET', 'POST'])
# def lista_articulos_crear_vista(request):
    
#     if request.method == 'GET':
#         articulos = Articulo.objects.filter(activo=True)
#         serializer = ArticuloSerializer(articulos, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticuloSerializer(data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def detalles_articulo_crear_vista(request, pk):
#     try:
#         articulo = Articulo.objects.get(pk=pk)
#     except Articulo.DoesNotExist:
#         return Response({
#             "error": {
#                 'codigo': 404,
#                 'mensaje': 'Articulo no encontrado'
#             }}, status=status.HTTP_404_NOT_FOUND)
    
#     if(request.method == 'GET'):
#         serializer = ArticuloSerializer(articulo)
#         return Response(serializer.data)
    
#     elif(request.method == 'PUT'):
#         serializer = ArticuloSerializer(articulo, data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         articulo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class lista_articulosAPIView(APIView):

    def get(self, request):
        articulos = Articulo.objects.filter(activo=True)
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticuloSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class detalles_articuloAPIView(APIView):
    def get_object(self, pk):
        articulo = get_object_or_404(Articulo, pk=pk)
        return articulo

    def get(self, request, pk):
        articulo = self.get_object(pk)
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)

    def put(self, request, pk):
        articulo = self.get_object(pk)
        serializer = ArticuloSerializer(articulo, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        articulo = self.get_object()
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

