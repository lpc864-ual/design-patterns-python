# Sin patrón Template Method
class InformeVentas:
    def generar_informe(self):
        # Conectar a la base de datos
        print("Conectando a la base de datos de ventas...")
        
        # Obtener datos
        print("Obteniendo datos de ventas...")
        
        # Procesamiento específico para informe de ventas
        print("Analizando tendencias de ventas por región...")
        print("Calculando ventas totales y comisiones...")
        
        # Generar resultado
        print("Generando gráficas de ventas...")
        
        # Enviar notificación
        print("Enviando informe de ventas por email a los gerentes...")
        
        print("Informe de ventas completado.\n")

class InformeInventario:
    def generar_informe(self):
        # Conectar a la base de datos
        print("Conectando a la base de datos de inventario...")
        
        # Obtener datos
        print("Obteniendo datos de inventario...")
        
        # Procesamiento específico para informe de inventario
        print("Identificando productos con bajo stock...")
        print("Calculando valor total del inventario...")
        
        # Generar resultado
        print("Generando listado de productos a reabastecer...")
        
        # Enviar notificación
        print("Enviando informe de inventario por email al departamento de compras...")
        
        print("Informe de inventario completado.\n")

# Cliente
informe_ventas = InformeVentas()
informe_ventas.generar_informe()

informe_inventario = InformeInventario()
informe_inventario.generar_informe()

# Problemas:
# - Duplicación de código (conectar a BD, obtener datos, enviar notificación)
# - Difícil mantener consistencia entre distintos tipos de informes
# - Cambios en el proceso general afectan a múltiples clases
# - No hay un control centralizado del flujo del algoritmo