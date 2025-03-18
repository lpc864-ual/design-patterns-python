# Sin patrón Observer
class EstacionMeteorologica:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0
        self.presion = 0
        
        # Referencia directa a las pantallas
        self.pantalla_actual = None
        self.pantalla_estadisticas = None
        self.app_movil = None
    
    def establecer_pantallas(self, actual, estadisticas, movil):
        self.pantalla_actual = actual
        self.pantalla_estadisticas = estadisticas
        self.app_movil = movil
    
    def actualizar_mediciones(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion
        
        # Notificar a cada pantalla directamente
        if self.pantalla_actual:
            self.pantalla_actual.actualizar(temperatura, humedad, presion)
        
        if self.pantalla_estadisticas:
            self.pantalla_estadisticas.actualizar(temperatura, humedad, presion)
        
        if self.app_movil:
            self.app_movil.actualizar(temperatura, humedad, presion)

class PantallaCondicionesActuales:
    def actualizar(self, temperatura, humedad, presion):
        print(f"Condiciones actuales: {temperatura}°C, {humedad}% humedad")

class PantallaEstadisticas:
    def __init__(self):
        self.temperaturas = []
    
    def actualizar(self, temperatura, humedad, presion):
        self.temperaturas.append(temperatura)
        temp_promedio = sum(self.temperaturas) / len(self.temperaturas)
        print(f"Estadísticas - Temperatura promedio: {temp_promedio:.1f}°C")

class AppMovil:
    def actualizar(self, temperatura, humedad, presion):
        print(f"App Móvil - Pronóstico: {temperatura}°C, {presion} hPa")

# Cliente
estacion = EstacionMeteorologica()
pantalla1 = PantallaCondicionesActuales()
pantalla2 = PantallaEstadisticas()
app = AppMovil()

# Configurar referencias
estacion.establecer_pantallas(pantalla1, pantalla2, app)

# Actualizar mediciones
print("Primera medición:")
estacion.actualizar_mediciones(25.5, 60, 1013)

print("\nSegunda medición:")
estacion.actualizar_mediciones(26.2, 58, 1012)

# Problemas:
# - Acoplamiento elevado: la estación debe conocer todas las pantallas
# - Difícil añadir nuevas pantallas o eliminar existentes
# - La estación debe mantener referencias a todos los observadores
# - No hay una interfaz estandarizada para los observadores