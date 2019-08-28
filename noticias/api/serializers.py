from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from noticias.models import Articulo, Escritor

class EscritorSerializer(serializers.ModelSerializer):
    articulos = serializers.StringRelatedField()
    
    class Meta:
        model = Escritor
        fields = "__all__"

class ArticuloSerializer(serializers.ModelSerializer):

    tiempo_desde_publicacion = serializers.SerializerMethodField()
    autor = serializers.StringRelatedField()
    autorEnlace = serializers.SerializerMethodField()
    enlacePropio = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        exclude = (['id'])
        # fields = '__all__'
        # fields = ('titulo, descripcion')

    def get_tiempo_desde_publicacion(self, object):
        fecha_pub = object.fecha_publicacion
        now = datetime.now()
        time_delta = timesince(fecha_pub, now)
        return time_delta

    def get_autorEnlace(self, object):
        return 'enlace la autor'

    def get_enlacePropio(self, object):
        return 'enlace url a este articulo particular'

    
    def validate(self, data):
        """Comprueba que la descipcion y el titulo sean distintos"""
        if(data['titulo'] == data['descripcion']):
            raise serializers.ValidationError("El titulo y la descripcion no deben ser iguales")
        return data
    
    def validate_titulo(self, value):
        if len(value) < 40:
            raise serializers.ValidationError("Por politica editorial, los titulos deben tener mas de 40 caracteres")
        return value


# class ArticuloSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     autor = serializers.CharField()
#     titulo = serializers.CharField()
#     descripcion = serializers.CharField()
#     cuerpo = serializers.CharField()
#     ubicacion = serializers.CharField()
#     fecha_publicacion = serializers.DateField()
#     activo = serializers.BooleanField()
#     fecha_creado = serializers.DateField(read_only=True)
#     fecha_actualizado = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Articulo.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.autor = validated_data.get('autor', instance.autor)
#         instance.titulo = validated_data.get('titulo', instance.titulo)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.cuerpo = validated_data.get('cuerpo', instance.cuerpo)
#         instance.ubicacion = validated_data.get('ubicacion', instance.ubicacion)
#         instance.fecha_publicacion = validated_data.get('fecha_publicacion', instance.fecha_publicacion)
#         instance.activo = validated_data.get('activo', instance.activo)
#         instance.save()
#         return instance
        

#     def validate(self, data):
#         """Comprueba que la descipcion y el titulo sean distintos"""
#         if(data['titulo'] == data['descripcion']):
#             raise serializers.ValidationError("El titulo y la descripcion no deben ser iguales")
#         return data
    
#     def validate_titulo(self, value):
#         if len(value) < 40:
#             raise serializers.ValidationError("Por politica editorial, los titulos deben tener mas de 40 caracteres")
#         return value