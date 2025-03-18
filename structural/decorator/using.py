# Con patrón Decorator
from abc import ABC, abstractmethod

# Componente
class CafeComponent(ABC):
    @abstractmethod
    def obtener_costo(self):
        pass
    
    @abstractmethod
    def obtener_descripcion(self):
        pass

# Componente concreto
class CafeSimple(CafeComponent):
    def obtener_costo(self):
        return 3.0
    
    def obtener_descripcion(self):
        return "Café básico"

# Decorador base
class CafeDecorator(CafeComponent):
    def __init__(self, cafe):
        self.cafe = cafe
    
    def obtener_costo(self):
        return self.cafe.obtener_costo()
    
    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion()

# Decoradores concretos
class ConLeche(CafeDecorator):
    def obtener_costo(self):
        return self.cafe.obtener_costo() + 1.0
    
    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + ", con leche"

class ConAzucar(CafeDecorator):
    def obtener_costo(self):
        return self.cafe.obtener_costo() + 0.5
    
    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + ", con azúcar"

class ConChocolate(CafeDecorator):
    def obtener_costo(self):
        return self.cafe.obtener_costo() + 1.5
    
    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + ", con chocolate"

class ConCanela(CafeDecorator):
    def obtener_costo(self):
        return self.cafe.obtener_costo() + 0.75
    
    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + ", con canela"

# Cliente
# Café básico
cafe_simple = CafeSimple()
print(f"{cafe_simple.obtener_descripcion()} - ${cafe_simple.obtener_costo()}")

# Café con leche
cafe_con_leche = ConLeche(CafeSimple())
print(f"{cafe_con_leche.obtener_descripcion()} - ${cafe_con_leche.obtener_costo()}")

# Café con leche y chocolate
cafe_leche_chocolate = ConChocolate(ConLeche(CafeSimple()))
print(f"{cafe_leche_chocolate.obtener_descripcion()} - ${cafe_leche_chocolate.obtener_costo()}")

# Fácilmente podemos crear combinaciones sin crear nuevas clases
cafe_completo = ConCanela(ConAzucar(ConChocolate(ConLeche(CafeSimple()))))
print(f"{cafe_completo.obtener_descripcion()} - ${cafe_completo.obtener_costo()}")