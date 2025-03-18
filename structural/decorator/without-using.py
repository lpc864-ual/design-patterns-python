# Sin patrón Decorator
class Cafe:
    def obtener_costo(self):
        return 3.0
    
    def obtener_descripcion(self):
        return "Café básico"

class CafeConLeche(Cafe):
    def obtener_costo(self):
        return super().obtener_costo() + 1.0
    
    def obtener_descripcion(self):
        return super().obtener_descripcion() + ", con leche"

class CafeConLecheYAzucar(CafeConLeche):
    def obtener_costo(self):
        return super().obtener_costo() + 0.5
    
    def obtener_descripcion(self):
        return super().obtener_descripcion() + " y azúcar"

class CafeConChocolate(Cafe):
    def obtener_costo(self):
        return super().obtener_costo() + 1.5
    
    def obtener_descripcion(self):
        return super().obtener_descripcion() + ", con chocolate"

class CafeConLecheYChocolate(CafeConLeche):
    def obtener_costo(self):
        return super().obtener_costo() + 1.5
    
    def obtener_descripcion(self):
        return super().obtener_descripcion() + " y chocolate"

# Cliente
cafe_simple = Cafe()
print(f"{cafe_simple.obtener_descripcion()} - ${cafe_simple.obtener_costo()}")

cafe_con_leche = CafeConLeche()
print(f"{cafe_con_leche.obtener_descripcion()} - ${cafe_con_leche.obtener_costo()}")

cafe_completo = CafeConLecheYChocolate()
print(f"{cafe_completo.obtener_descripcion()} - ${cafe_completo.obtener_costo()}")

# Problema: explosión de clases para cada combinación posible
# ¿Y si queremos agregar más ingredientes como canela, crema, etc.?