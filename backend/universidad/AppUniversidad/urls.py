from django.urls import path, include
from rest_framework import routers
from .views import AdminViewSet, CarreraViewSet, SeccionViewSet, ProfesorViewSet, MateriasViewSet, MateriasCursadasViewSet, EstudianteViewSet


router = routers.DefaultRouter()
router.register(r"administradores", AdminViewSet)
router.register(r"secciones", SeccionViewSet)
router.register(r"profesores", ProfesorViewSet)
router.register(r"materias", MateriasViewSet)
router.register(r"materias_cursadas", MateriasCursadasViewSet)
router.register(r"carreras", CarreraViewSet)
router.register(r"estudiantes", EstudianteViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework"))
]
