# Con patrón Proxy
from abc import ABC, abstractmethod

# Sujeto abstracto
class Imagen(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Sujeto real
class ImagenReal(Imagen):
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self._cargar_imagen()
    
    def _cargar_imagen(self):
        print(f"Cargando imagen desde el disco: {self.nombre_archivo}")
        # Simulamos una carga pesada
        import time
        time.sleep(1)  # Simulación de carga de imagen (1 segundo)
    
    def mostrar(self):
        print(f"Mostrando imagen: {self.nombre_archivo}")

# Proxy
class ProxyImagen(Imagen):
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.imagen_real = None
    
    def mostrar(self):
        # Carga diferida: solo carga la imagen real cuando es necesario
        if self.imagen_real is None:
            self.imagen_real = ImagenReal(self.nombre_archivo)
        
        # Delega la visualización a la imagen real
        self.imagen_real.mostrar()

# Cliente
def galeria_imagenes_con_proxy():
    # Crear proxies de imágenes (sin cargar las imágenes reales)
    imagenes = [
        ProxyImagen("imagen1.jpg"),
        ProxyImagen("imagen2.jpg"),
        ProxyImagen("imagen3.jpg"),
        ProxyImagen("imagen4.jpg"),
        ProxyImagen("imagen5.jpg")
    ]
    
    print("\nNota: Las imágenes aún no se han cargado, solo tenemos proxies")
    
    # Ahora cada imagen se carga solo cuando se accede a ella
    for i, imagen in enumerate(imagenes):
        if i % 2 == 0:  # Usuario solo ve algunas imágenes
            print(f"\nUsuario hace clic en la imagen {i+1}:")
            imagen.mostrar()  # Solo ahora se carga la imagen real

# Ejecutar galería con proxy
galeria_imagenes_con_proxy()

# Otros tipos de proxies incluyen:
# - Proxy de protección: controla el acceso al objeto basado en permisos
# - Proxy remoto: representa un objeto ubicado en un espacio de direcciones diferente
# - Proxy de registro: guarda información sobre el acceso al objeto