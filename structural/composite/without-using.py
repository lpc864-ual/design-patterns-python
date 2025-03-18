# Sin patrón Composite
class Archivo:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
    
    def mostrar(self, nivel=0):
        return "  " * nivel + f"Archivo: {self.nombre} ({self.tamaño} KB)"

class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = []
        self.subcarpetas = []
    
    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)
    
    def agregar_carpeta(self, carpeta):
        self.subcarpetas.append(carpeta)
    
    def mostrar(self, nivel=0):
        resultado = "  " * nivel + f"Carpeta: {self.nombre}\n"
        
        # Mostrar archivos
        for archivo in self.archivos:
            resultado += archivo.mostrar(nivel + 1) + "\n"
        
        # Mostrar subcarpetas
        for carpeta in self.subcarpetas:
            resultado += carpeta.mostrar(nivel + 1)
        
        return resultado
    
    def obtener_tamaño(self):
        tamaño_total = 0
        
        # Sumar tamaño de archivos
        for archivo in self.archivos:
            tamaño_total += archivo.tamaño
        
        # Sumar tamaño de subcarpetas
        for carpeta in self.subcarpetas:
            tamaño_total += carpeta.obtener_tamaño()
        
        return tamaño_total

# Cliente
# Notar que debemos tratar archivos y carpetas de forma diferente
archivo1 = Archivo("documento.txt", 5)
archivo2 = Archivo("imagen.jpg", 20)
archivo3 = Archivo("video.mp4", 200)

carpeta1 = Carpeta("Documentos")
carpeta1.agregar_archivo(archivo1)

carpeta2 = Carpeta("Multimedia")
carpeta2.agregar_archivo(archivo2)
carpeta2.agregar_archivo(archivo3)

carpeta_raiz = Carpeta("Raíz")
carpeta_raiz.agregar_carpeta(carpeta1)
carpeta_raiz.agregar_carpeta(carpeta2)

# El cliente debe saber cuál método llamar dependiendo del tipo de objeto
print(carpeta_raiz.mostrar())
print(f"Tamaño total: {carpeta_raiz.obtener_tamaño()} KB")
print(f"Tamaño de archivo individual: {archivo1.tamaño} KB")  # No tiene método obtener_tamaño()