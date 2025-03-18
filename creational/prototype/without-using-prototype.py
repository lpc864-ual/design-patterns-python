# Sin patrón Prototype
class Documento:
    def __init__(self, tipo, contenido, estilo, cabecera, pie_pagina, numeracion):
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

# Cliente
# Crea un documento de informe
informe_original = Documento(
    "Informe", 
    "Contenido del informe", 
    "Corporativo", 
    "Informe Trimestral", 
    "Confidencial", 
    True
)

# Para crear un informe similar, tenemos que volver a especificar todos los parámetros
informe_modificado = Documento(
    "Informe", 
    "Contenido actualizado del informe", 
    "Corporativo", 
    "Informe Trimestral", 
    "Confidencial", 
    True
)

# Y otra vez para otro documento, con mucha duplicación
informe_otro = Documento(
    "Informe", 
    "Contenido de otro informe", 
    "Corporativo", 
    "Informe Trimestral", 
    "Público", 
    True
)

print(informe_otro)