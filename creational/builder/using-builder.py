# Con patrón Builder
class Coche:
    def __init__(self):
        # Atributos obligatorios
        self.marca = None
        self.modelo = None
        
        # Opciones configurables
        self.motor = None
        self.transmision = None
        self.navegacion = False
        self.asientos_calefactados = False
        self.sensores_estacionamiento = False
        self.camara_trasera = False
        self.asistente_carril = False
    
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

class ConstructorCoche:
    def __init__(self):
        self.coche = Coche()
    
    def establecer_marca_modelo(self, marca, modelo):
        self.coche.marca = marca
        self.coche.modelo = modelo
        return self
    
    def establecer_motor(self, motor):
        self.coche.motor = motor
        return self
    
    def establecer_transmision(self, transmision):
        self.coche.transmision = transmision
        return self
    
    def añadir_navegacion(self):
        self.coche.navegacion = True
        return self
    
    def añadir_asientos_calefactados(self):
        self.coche.asientos_calefactados = True
        return self
    
    def añadir_sensores_estacionamiento(self):
        self.coche.sensores_estacionamiento = True
        return self
    
    def añadir_camara_trasera(self):
        self.coche.camara_trasera = True
        return self
    
    def añadir_asistente_carril(self):
        self.coche.asistente_carril = True
        return self
    
    def construir(self):
        return self.coche

# Director (opcional)
class DirectorCoche:
    @staticmethod
    def construir_coche_base(constructor):
        return (constructor
                .establecer_marca_modelo("Toyota", "Corolla")
                .establecer_motor("1.6L")
                .establecer_transmision("Manual")
                .construir())
    
    @staticmethod
    def construir_coche_lujo(constructor):
        return (constructor
                .establecer_marca_modelo("BMW", "Serie 5")
                .establecer_motor("3.0L")
                .establecer_transmision("Automática")
                .añadir_navegacion()
                .añadir_asientos_calefactados()
                .añadir_sensores_estacionamiento()
                .añadir_camara_trasera()
                .añadir_asistente_carril()
                .construir())

# Cliente
# Usando el director para configuraciones predefinidas
constructor = ConstructorCoche()
coche_base = DirectorCoche.construir_coche_base(constructor)

constructor = ConstructorCoche()
coche_lujo = DirectorCoche.construir_coche_lujo(constructor)

# O construyendo manualmente para mayor flexibilidad
constructor = ConstructorCoche()
coche_personalizado = (constructor
                       .establecer_marca_modelo("Honda", "Civic")
                       .establecer_motor("2.0L")
                       .establecer_transmision("Automática")
                       .añadir_navegacion()
                       .añadir_sensores_estacionamiento()
                       .añadir_camara_trasera()
                       .construir())

print(coche_personalizado)