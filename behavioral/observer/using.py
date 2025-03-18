# Con patrón Observer
from abc import ABC, abstractmethod

# Sujeto (interfaz)
class Sujeto(ABC):
    @abstractmethod
    def registrar_observador(self, observador):
        pass
    
    @abstractmethod
    def eliminar_observador(self, observador):
        pass
    
    @abstractmethod
    def notificar_observadores(self):
        pass

# Observador (interfaz)
class Observador(ABC):
    @abstractmethod
    def actualizar(self, temperatura, humedad, presion):
        pass

# Sujeto concreto
class EstacionMeteorologica(Sujeto):
    def __init__(self):
        self.observadores = []
        self.temperatura = 0
        self.humedad = 0
        self.presion = 0
    
    def registrar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)
    
    def eliminar_observador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
    
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self.temperatura, self.humedad, self.presion)
    
    def actualizar_mediciones(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion
        self.mediciones_cambiaron()
    
    def mediciones_cambiaron(self):
        self.notificar_observadores()

# Observadores concretos
class PantallaCondicionesActuales(Observador):
    def __init__(self, estacion_meteorologica):
        self.estacion_meteorologica = estacion_meteorologica
        self.estacion_meteorologica.registrar_observador(self)
    
    def actualizar(self, temperatura, humedad, presion):
        print(f"Condiciones actuales: {temperatura}°C, {humedad}% humedad")

class PantallaEstadisticas(Observador):
    def __init__(self, estacion_meteorologica):
        self.estacion_meteorologica = estacion_meteorologica
        self.estacion_meteorologica.registrar_observador(self)
        self.temperaturas = []
    
    def actualizar(self, temperatura, humedad, presion):
        self.temperaturas.append(temperatura)
        temp_promedio = sum(self.temperaturas) / len(self.temperaturas)
        print(f"Estadísticas - Temperatura promedio: {temp_promedio:.1f}°C")

class AppMovil(Observador):
    def __init__(self, estacion_meteorologica):
        self.estacion_meteorologica = estacion_meteorologica
        self.estacion_meteorologica.registrar_observador(self)
    
    def actualizar(self, temperatura, humedad, presion):
        print(f"App Móvil - Pronóstico: {temperatura}°C, {presion} hPa")
    
    # Método específico para desuscribirse cuando se cierra la app
    def cerrar_app(self):
        self.estacion_meteorologica.eliminar_observador(self)
        print("App cerrada y desuscrita de actualizaciones")

# Cliente
estacion = EstacionMeteorologica()

# Crear observadores (se registran automáticamente en el constructor)
pantalla1 = PantallaCondicionesActuales(estacion)
pantalla2 = PantallaEstadisticas(estacion)
app = AppMovil(estacion)

# Actualizar mediciones
print("Primera medición:")
estacion.actualizar_mediciones(25.5, 60, 1013)

print("\nSegunda medición:")
estacion.actualizar_mediciones(26.2, 58, 1012)

# El usuario cierra la app
print("\nUsuario cierra la app:")
app.cerrar_app()

# La próxima actualización solo notifica a las pantallas activas
print("\nTercera medición (sin app):")
estacion.actualizar_mediciones(24.8, 62, 1014)

# Añadir un nuevo observador en tiempo de ejecución
class PantallaPronostico(Observador):
    def actualizar(self, temperatura, humedad, presion):
        tendencia = "estable"
        if presion < 1000:
            tendencia = "lluvioso"
        elif presion > 1020:
            tendencia = "soleado"
        print(f"Pronóstico: Tendencia {tendencia}")

print("\nAñadiendo nuevo observador (Pronóstico):")
pronostico = PantallaPronostico()
estacion.registrar_observador(pronostico)

print("\nCuarta medición (con pronóstico):")
estacion.actualizar_mediciones(23.9, 65, 1007)

# Ventajas:
# - Bajo acoplamiento: el sujeto solo conoce la interfaz del observador
# - Comunicación broadcast: un cambio notifica a todos los interesados
# - Abierto/cerrado: nuevos observadores pueden añadirse sin modificar el sujeto
# - Relaciones establecidas en tiempo de ejecución