# Sin patrón Proxy
class Imagen:
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

# Cliente
def galeria_imagenes():
    imagenes = [
        Imagen("imagen1.jpg"),
        Imagen("imagen2.jpg"),
        Imagen("imagen3.jpg"),
        Imagen("imagen4.jpg"),
        Imagen("imagen5.jpg")
    ]
    
    print("\nNota: Todas las imágenes se cargaron inmediatamente al ser creadas")
    
    # El usuario puede nunca ver algunas imágenes, pero todas se cargan
    for i, imagen in enumerate(imagenes):
        if i % 2 == 0:  # Usuario solo ve algunas imágenes
            print(f"\nUsuario hace clic en la imagen {i+1}:")
            imagen.mostrar()

# Ejecutar galería
galeria_imagenes()