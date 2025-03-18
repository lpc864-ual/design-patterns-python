# Con patrón Template Method
from abc import ABC, abstractmethod

# Clase abstracta con el método plantilla
class Informe(ABC):
    # Método plantilla que define el algoritmo
    def generar_informe(self):
        self.conectar_bd()
        self.obtener_datos()
        self.analizar_datos()
        self.generar_visualizacion()
        self.enviar_notificacion()
        if self.requiere_archivo_respaldo():  # Hook method
            self.crear_archivo_respaldo()
        print(f"Informe de {self.tipo_informe()} completado.\n")
    
    # Métodos comunes con implementación por defecto
    def conectar_bd(self):
        print(f"Conectando a la base de datos de {self.tipo_informe()}...")
    
    def obtener_datos(self):
        print(f"Obteniendo datos de {self.tipo_informe()}...")
    
    def enviar_notificacion(self):
        print(f"Enviando informe de {self.tipo_informe()} por email...")
    
    # Hook method con implementación por defecto
    def requiere_archivo_respaldo(self):
        return False
    
    def crear_archivo_respaldo(self):
        print(f"Creando archivo de respaldo del informe de {self.tipo_informe()}...")
    
    # Métodos abstractos que las subclases deben implementar
    @abstractmethod
    def tipo_informe(self):
        pass
    
    @abstractmethod
    def analizar_datos(self):
        pass
    
    @abstractmethod
    def generar_visualizacion(self):
        pass

# Clases concretas
class InformeVentas(Informe):
    def tipo_informe(self):
        return "ventas"
    
    def analizar_datos(self):
        print("Analizando tendencias de ventas por región...")
        print("Calculando ventas totales y comisiones...")
    
    def generar_visualizacion(self):
        print("Generando gráficas de ventas...")
    
    def enviar_notificacion(self):
        print("Enviando informe de ventas por email a los gerentes...")
    
    # Sobreescribir hook method
    def requiere_archivo_respaldo(self):
        return True

class InformeInventario(Informe):
    def tipo_informe(self):
        return "inventario"
    
    def analizar_datos(self):
        print("Identificando productos con bajo stock...")
        print("Calculando valor total del inventario...")
    
    def generar_visualizacion(self):
        print("Generando listado de productos a reabastecer...")
    
    def enviar_notificacion(self):
        print("Enviando informe de inventario por email al departamento de compras...")

# Añadir una nueva clase de informe es sencillo
class InformeClientes(Informe):
    def tipo_informe(self):
        return "clientes"
    
    def analizar_datos(self):
        print("Segmentando clientes por frecuencia de compra...")
        print("Identificando clientes inactivos...")
    
    def generar_visualizacion(self):
        print("Generando dashboard de retención de clientes...")

# Cliente
informe_ventas = InformeVentas()
informe_ventas.generar_informe()

informe_inventario = InformeInventario()
informe_inventario.generar_informe()

informe_clientes = InformeClientes()
informe_clientes.generar_informe()

# Ventajas:
# - Código reutilizable en la clase base
# - Control centralizado del algoritmo
# - Extensible mediante especialización
# - Las subclases solo implementan los pasos específicos que necesitan
# - Hooks methods para extensiones opcionales