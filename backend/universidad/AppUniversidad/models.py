from django.db import models

# Create your models here.
class AdminModel( models.Model ):
    imgPerfil = models.ImageField( upload_to="admin/profile" )
    nombre = models.CharField( max_length=100 )
    apellido = models.CharField( max_length=100 )
    email = models.EmailField()
    contrasena = models.CharField( max_length=50 )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    

class CarrerasModel( models.Model ):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    

class SeccionModel( models.Model ):
    numeroSeccion = models.IntegerField()
    ubicacion = models.CharField( max_length=100 )
    carrera = models.ForeignKey(CarrerasModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numeroSeccion
    

class ProfesorModel( models.Model ):
    imgPerfil = models.ImageField( upload_to="profesor/profile" )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    

class MateriasModel( models.Model ):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey( CarrerasModel, on_delete=models.CASCADE )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

class MateriaCursadaModel( models.Model ):
    materia = models.ForeignKey(CarrerasModel, on_delete=models.CASCADE)
    profesor = models.ForeignKey( ProfesorModel, on_delete = models.CASCADE )
    seccion = models.ForeignKey( SeccionModel, on_delete=models.CASCADE )
    calificacion = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.materia
    

class EstudiantesModel( models.Model ):
    imgPerfil = models.ImageField( upload_to="estudiante/profile" )
    matricula = models.SlugField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    carrera = models.OneToOneField( CarrerasModel, on_delete=models.CASCADE )
    materiasCursadas = models.ManyToManyField(MateriasModel)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class PruebasModel:
    nombre = models.CharField(max_length=50)