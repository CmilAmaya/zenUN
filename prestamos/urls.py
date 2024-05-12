from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

#Rutas de la aplicación "Usuarios"
urlpatterns = [
        path('solicitarPrestamo/', 
            views.mostrar_solicitarPrestamo, 
            name='solicitarPrestamo'
        ), #Vista solicitarPrestamo
        path('devolucionImplementos/', 
            views.mostrar_devolucionImplementos_administradorBienestar, 
            name='devolucionImplementos'
        ), #Vista devolucionImplementos
        path("devolucionImplementos/informacionPrestamo/",
            views.mostrar_informacionPrestamo_devolucionImplementos_administradorBienestar,
            name="devolucionImplementos_mostrarInformacionPrestamo"
        ), #En la vista  devolucionImplementos mostrar la informacion del prestamo
        path('devolucionImplementos/informacionPrestamo/<str:numeroDocumento>/', 
            views.mostrar_devolucionImplementosConParametroNumeroDocumento_administradorBienestar, 
            name='devolucionImplementosConParametroNumeroDocumento'
        ), # Vista devolucionImplementos( con paramentro CORREO en la URL) 
        path("devolucionImplementos/informacionPrestamo/<str:numeroDocumento>/procesarDevolucion/",
            views.procesar_devolucion_devolucionImplementos_administradorBienestar,
            name="devolucionImplementos_procesarDevolucion"
        ), #En la vista  devolucionImplementos( con paramentro CORREO en la URL)  procesar devolucion implemento
        ##vista Disponibilidad Implementos
        path('tablaDisponibilidadImplementos/', 
             login_required(views.mostrar_tabla_disponibilidad_implementos), 
             name='tablaDisponibilidadImplementos'),
        ## Ejemplo Pasar los parametros a la vista solicitar Prestamo
        path('solicitarPrestamo/<int:implemento_id>/', 
             views.solicitar_prestamo, 
             name='solicitar_prestamo'),
        path('reservar-implemento/<int:implemento_id>/', views.reservar_implemento, name='reservar_implemento'),
]