from rest_framework import viewsets
from .models import AdminModel, CarrerasModel, SeccionModel,ProfesorModel, MateriasModel, MateriaCursadaModel,EstudiantesModel 
from .serializers import AdminSerializer, CarreraSerializer, SeccionSerializer, ProfesorSerializer, MateriaSerializer, MateriasCursadasSerializer, EstudiantesSerializer

class AdminViewSet( viewsets.ModelViewSet ):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer


class CarreraViewSet( viewsets.ModelViewSet ):
    queryset = CarrerasModel.objects.all()
    serializer_class = CarreraSerializer

class SeccionViewSet( viewsets.ModelViewSet ):
    queryset = SeccionModel.objects.all()
    serializer_class = SeccionSerializer

class ProfesorViewSet( viewsets.ModelViewSet ):
    queryset = ProfesorModel.objects.all()
    serializer_class = ProfesorSerializer

class MateriasViewSet( viewsets.ModelViewSet ):
    queryset = MateriasModel.objects.all()
    serializer_class = MateriaSerializer

class MateriasCursadasViewSet( viewsets.ModelViewSet ):
    queryset = MateriaCursadaModel.objects.all()
    serializer_class = MateriasCursadasSerializer

class EstudianteViewSet( viewsets.ModelViewSet ):
    queryset = EstudiantesModel.objects.all()
    serializer_class = EstudiantesSerializer

