# Con patrón Prototype
import copy

class Documento:
    def __init__(self, tipo=None, contenido=None, estilo=None, cabecera=None, pie_pagina=None, numeracion=None):
        self.tipo = tipo
        self.contenido = contenido
        self.estilo = estilo
        self.cabecera = cabecera
        self.pie_pagina = pie_pagina
        self.numeracion = numeracion
    
    def __str__(self):
        return f"""
        Documento {self.tipo}
        Contenido: {self.contenido}
        Estilo: {self.estilo}
        Cabecera: {self.cabecera}
        Pie de página: {self.pie_pagina}
        Numeración: {self.numeracion}
        """
    
    def clonar(self):
        # Uso de deepcopy para asegurar que todos los objetos anidados también se copien
        return copy.deepcopy(self)

# Cliente
# Crear un prototipo de documento de informe
prototipo_informe = Documento(
    "Informe", 
    "Contenido base", 
    "Corporativo", 
    "Informe Trimestral", 
    "Confidencial", 
    True
)

# Registrar prototipos en un diccionario (opcional)
prototipos = {
    "informe": prototipo_informe,
    # Podríamos añadir más prototipos aquí
}

# Clonar y modificar sólo lo necesario
informe_modificado = prototipos["informe"].clonar()
informe_modificado.contenido = "Contenido actualizado del informe"

# Clonar y modificar otro aspecto
informe_otro = prototipos["informe"].clonar()
informe_otro.contenido = "Contenido de otro informe"
informe_otro.pie_pagina = "Público"

print(informe_otro)