# Con patrón Strategy
from abc import ABC, abstractmethod

# Estrategia (interfaz)
class EstrategiaImpuesto(ABC):
    @abstractmethod
    def calcular(self, monto):
        pass

# Estrategias concretas
class EstrategiaIVA(EstrategiaImpuesto):
    def calcular(self, monto):
        return monto * 0.21

class EstrategiaIRPF(EstrategiaImpuesto):
    def calcular(self, monto):
        if monto <= 30000:
            return monto * 0.15
        else:
            return 30000 * 0.15 + (monto - 30000) * 0.20

class EstrategiaIS(EstrategiaImpuesto):
    def calcular(self, monto):
        base_imponible = monto * 0.90  # 10% de gastos deducibles
        return base_imponible * 0.25

# Contexto
class CalculadoraImpuestos:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia
    
    def establecer_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def calcular_impuesto(self, monto):
        if self.estrategia is None:
            raise ValueError("No se ha establecido una estrategia de cálculo")
        return self.estrategia.calcular(monto)

# Cliente
# Crear estrategias
estrategia_iva = EstrategiaIVA()
estrategia_irpf = EstrategiaIRPF()
estrategia_is = EstrategiaIS()

# Crear calculadora
calculadora = CalculadoraImpuestos()

# Calcular IVA
calculadora.establecer_estrategia(estrategia_iva)
monto_compra = 1000
impuesto_iva = calculadora.calcular_impuesto(monto_compra)
print(f"Impuesto IVA para {monto_compra}€: {impuesto_iva}€")

# Calcular IRPF
calculadora.establecer_estrategia(estrategia_irpf)
salario_anual = 45000
impuesto_renta = calculadora.calcular_impuesto(salario_anual)
print(f"Impuesto sobre la renta para {salario_anual}€: {impuesto_renta}€")

# Calcular IS
calculadora.establecer_estrategia(estrategia_is)
beneficio_empresa = 100000
impuesto_sociedades = calculadora.calcular_impuesto(beneficio_empresa)
print(f"Impuesto de sociedades para {beneficio_empresa}€: {impuesto_sociedades}€")

# Añadir una nueva estrategia sin modificar el código existente
class EstrategiaAutonomos(EstrategiaImpuesto):
    def calcular(self, monto):
        if monto <= 12000:
            return monto * 0.07
        elif monto <= 30000:
            return 12000 * 0.07 + (monto - 12000) * 0.15
        else:
            return 12000 * 0.07 + 18000 * 0.15 + (monto - 30000) * 0.20

# Usar la nueva estrategia
estrategia_autonomos = EstrategiaAutonomos()
calculadora.establecer_estrategia(estrategia_autonomos)
ingresos_autonomo = 25000
impuesto_autonomo = calculadora.calcular_impuesto(ingresos_autonomo)
print(f"Impuesto para autónomo con {ingresos_autonomo}€: {impuesto_autonomo}€")

# Ventajas:
# - Separación clara entre contexto y algoritmos
# - Fácil añadir nuevos algoritmos sin modificar el código existente
# - Los algoritmos son intercambiables en tiempo de ejecución
# - Mejor organización y responsabilidad única
# - Cumple con el principio Open/Closed