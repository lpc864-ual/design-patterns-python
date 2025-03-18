# Sin patrón Builder
class Coche:
    def __init__(self, marca, modelo, motor, transmision, navegacion, asientos_calefactados, sensores_estacionamiento, camara_trasera, asistente_carril):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.transmision = transmision
        self.navegacion = navegacion
        self.asientos_calefactados = asientos_calefactados
        self.sensores_estacionamiento = sensores_estacionamiento
        self.camara_trasera = camara_trasera
        self.asistente_carril = asistente_carril
    
    def __str__(self):
        return f"""
        Coche: {self.marca} {self.modelo}
        Motor: {self.motor}
        Transmisión: {self.transmision}
        Navegación: {'Sí' if self.navegacion else 'No'}
        Asientos calefactados: {'Sí' if self.asientos_calefactados else 'No'}
        Sensores de estacionamiento: {'Sí' if self.sensores_estacionamiento else 'No'}
        Cámara trasera: {'Sí' if self.camara_trasera else 'No'}
        Asistente de carril: {'Sí' if self.asistente_carril else 'No'}
        """

# Cliente
# Demasiados parámetros, propenso a errores y difícil de leer
coche_base = Coche("Toyota", "Corolla", "1.6L", "Manual", False, False, False, False, False)
coche_lujo = Coche("BMW", "Serie 5", "3.0L", "Automática", True, True, True, True, True)

# Si queremos un coche semi-personalizado, es complejo y poco legible
coche_personalizado = Coche("Honda", "Civic", "2.0L", "Automática", True, False, True, True, False)

print(coche_personalizado)