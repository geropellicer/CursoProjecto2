from rest_framework import serializers
from noticias.models import Articulo


class ArticuloSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    autor = serializers.CharField()
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    cuerpo = serializers.CharField()
    ubicacion = serializers.CharField()
    fecha_publicacion = serializers.DateField()
    activo = serializers.BooleanField()
    fecha_creado = serializers.DateField(read_only=True)
    fecha_actualizado = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Articulo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.autor = validated_data.get('autor', instance.autor)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.cuerpo = validated_data.get('cuerpo', instance.cuerpo)
        instance.ubicacion = validated_data.get('ubicacion', instance.ubicacion)
        instance.fecha_publicacion = validated_data.get('fecha_publicacion', instance.fecha_publicacion)
        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance
        

