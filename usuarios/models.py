from django.db import models
from simple_history.models import HistoricalRecords

#Modelo para la entidad Tipo de documento
class tipoDocumento(models.Model):
    idTipoDocumento = models.AutoField(primary_key=True)
    siglasTipoDocumento = models.CharField(max_length=5)
    descripcionTipoDocumento = models.CharField(max_length=45)

#Modelo para la entidad Rol
class rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=45)
    descripcionRol = models.CharField(max_length=255)


class razonCambio(models.Model):
    idCambio = models.AutoField(primary_key=True)
    razonCambio = models.CharField(max_length=255)

#Modelo para la entidad usuario
class usuario(models.Model):
    numeroDocumento = models.IntegerField(primary_key=True)
    idTipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE) #llave foránea
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correoInstitucional = models.CharField(max_length=50, unique=True) #UNIQUE para que no se pueda repetir el correo.
    password = models.CharField(max_length=255)
    numeroCelular = models.CharField(max_length=15)
    roles = models.ManyToManyField(rol) #Crea la relación muchos a muchos
    codigoVerificacion = models.IntegerField() #Campo INT para el proceso de verificación de correo
    usuarioVerificado = models.BooleanField(default=False) #Si es TRUE el usuario ha sido verificado    
    lastLogin = models.DateTimeField(null = True) #Mantiene registro de la última vez que inició sesión un usuario
    history = HistoricalRecords(history_change_reason_field=models.ForeignKey(razonCambio, null=True, on_delete=models.CASCADE),m2m_fields=[roles],table_name = 'trazabilidadUsuarios',cascade_delete_history=True)           
    USERNAME_FIELD = 'correoInstitucional'
    REQUIRED_FIELDS = [
        'numeroDocumento',
        'idTipoDocumento',
        'nombres',
        'apellidos',
        'numeroCelular',
        'codigoVerificacion',
        'usuarioVerificado',
    ]
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
       
