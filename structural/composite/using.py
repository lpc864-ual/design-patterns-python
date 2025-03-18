# Con patrón Composite
from abc import ABC, abstractmethod

# Componente (interfaz común)
class ComponenteArchivo(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def mostrar(self, nivel=0):
        pass
    
    @abstractmethod
    def obtener_tamaño(self):
        pass

# Hoja
class Archivo(ComponenteArchivo):
    def __init__(self, nombre, tamaño):
        super().__init__(nombre)
        self.tamaño = tamaño
    
    def mostrar(self, nivel=0):
        return "  " * nivel + f"Archivo: {self.nombre} ({self.tamaño} KB)"
    
    def obtener_tamaño(self):
        return self.tamaño

# Compuesto
class Carpeta(ComponenteArchivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []
    
    def agregar(self, componente):
        self.componentes.append(componente)
    
    def eliminar(self, componente):
        self.componentes.remove(componente)
    
    def mostrar(self, nivel=0):
        resultado = "  " * nivel + f"Carpeta: {self.nombre}\n"
        
        # Mostrar todos los componentes (archivos y subcarpetas)
        for componente in self.componentes:
            resultado += componente.mostrar(nivel + 1) + "\n"
        
        return resultado
    
    def obtener_tamaño(self):
        tamaño_total = 0
        
        # Sumar tamaño de todos los componentes
        for componente in self.componentes:
            tamaño_total += componente.obtener_tamaño()
        
        return tamaño_total

# Cliente
# Ahora tratamos archivos y carpetas de manera uniforme
archivo1 = Archivo("documento.txt", 5)
archivo2 = Archivo("imagen.jpg", 20)
archivo3 = Archivo("video.mp4", 200)

carpeta1 = Carpeta("Documentos")
carpeta1.agregar(archivo1)

carpeta2 = Carpeta("Multimedia")
carpeta2.agregar(archivo2)
carpeta2.agregar(archivo3)

carpeta_raiz = Carpeta("Raíz")
carpeta_raiz.agregar(carpeta1)
carpeta_raiz.agregar(carpeta2)

# El cliente trata todos los objetos de manera uniforme
print(carpeta_raiz.mostrar())
print(f"Tamaño total: {carpeta_raiz.obtener_tamaño()} KB")
print(f"Tamaño de archivo individual: {archivo1.obtener_tamaño()} KB")  # Interfaz uniforme

# Podemos tratar un archivo individual igual que una carpeta compleja
for componente in [archivo1, carpeta1, carpeta_raiz]:
    print(f"{componente.nombre}: {componente.obtener_tamaño()} KB")