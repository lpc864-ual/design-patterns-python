# Con patrón Chain of Responsibility
from abc import ABC, abstractmethod

# Manejador abstracto
class AprobadorGasto(ABC):
    def __init__(self):
        self._siguiente = None
    
    def establecer_siguiente(self, siguiente):
        self._siguiente = siguiente
        return siguiente  # Para permitir encadenamiento
    
    def aprobar(self, monto, proposito):
        if self._puede_aprobar(monto):
            return self._aprobar(monto, proposito)
        elif self._siguiente:
            # Pasar al siguiente en la cadena
            return self._siguiente.aprobar(monto, proposito)
        else:
            return f"Nadie puede aprobar un gasto de ${monto}"
    
    @abstractmethod
    def _puede_aprobar(self, monto):
        pass
    
    @abstractmethod
    def _aprobar(self, monto, proposito):
        pass

# Manejadores concretos
class LiderEquipo(AprobadorGasto):
    def _puede_aprobar(self, monto):
        return monto <= 100
    
    def _aprobar(self, monto, proposito):
        return f"Líder de equipo aprueba gasto de ${monto} para {proposito}"

class Gerente(AprobadorGasto):
    def _puede_aprobar(self, monto):
        return monto <= 1000
    
    def _aprobar(self, monto, proposito):
        return f"Gerente aprueba gasto de ${monto} para {proposito}"

class Director(AprobadorGasto):
    def _puede_aprobar(self, monto):
        return monto <= 10000
    
    def _aprobar(self, monto, proposito):
        return f"Director aprueba gasto de ${monto} para {proposito}"

class CEO(AprobadorGasto):
    def _puede_aprobar(self, monto):
        return monto <= 50000
    
    def _aprobar(self, monto, proposito):
        return f"CEO aprueba gasto de ${monto} para {proposito}"

# Cliente
# Configurar la cadena
lider = LiderEquipo()
gerente = Gerente()
director = Director()
ceo = CEO()

lider.establecer_siguiente(gerente).establecer_siguiente(director).establecer_siguiente(ceo)

# Usar la cadena - la solicitud encontrará automáticamente el nivel adecuado
print(lider.aprobar(50, "suministros de oficina"))
print(lider.aprobar(500, "equipo nuevo"))
print(lider.aprobar(5000, "conferencia"))
print(lider.aprobar(20000, "renovación de oficina"))
print(lider.aprobar(60000, "nuevo edificio"))  # Excede todos los límites

# Ventajas:
# - Fácil añadir o modificar manejadores
# - Desacoplamiento entre emisor y receptor
# - Flexibilidad para decidir quién maneja la solicitud en tiempo de ejecución