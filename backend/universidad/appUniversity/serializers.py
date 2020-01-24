from rest_framework import serializers
from .models import AdminModel, CarrerasModel, SeccionModel,ProfesorModel, MateriasModel, MateriaCursadaModel,EstudiantesModel 


class AdminSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = AdminModel
        fields = ['id', 'imgPerfil','nombre', 'apellido', 'email', 'contrasena', 'created', 'updated']


class CarreraSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = CarrerasModel
        fields = ['id','nombre', 'descripcion', 'created', 'updated']
    

class SeccionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = SeccionModel
        fields = ['id','numeroSeccion', 'ubicacion', 'carrera', 'created', 'updated']


class ProfesorSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta: 
        model = ProfesorModel
        fields = ['id', 'imgPerfil', 'nombre', 'apellido', 'created','updated']

class MateriaSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = MateriasModel
        fields = ['id', 'nombre','carrera', 'created','updated']


class MateriasCursadasSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = MateriaCursadaModel
        fields = ['id', 'materia', 'profesor', 'seccion', 'calificacion', 'created', 'updated']


class EstudiantesSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = EstudiantesModel
        fields = ['id','imgPerfil', 'matricula','nombre', 'apellido', 'carrera', 'materiasCursadas', 'created', 'updated']