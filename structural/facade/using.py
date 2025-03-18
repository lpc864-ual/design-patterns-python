# Con patrón Facade
class Amplificador:
    def encender(self):
        return "Amplificador encendido"
    
    def apagar(self):
        return "Amplificador apagado"
    
    def configurar_volumen(self, nivel):
        return f"Volumen configurado a {nivel}"
    
    def configurar_fuente(self, fuente):
        return f"Fuente configurada: {fuente}"

class ReproductorDVD:
    def encender(self):
        return "Reproductor DVD encendido"
    
    def apagar(self):
        return "Reproductor DVD apagado"
    
    def reproducir(self, pelicula):
        return f"Reproduciendo '{pelicula}'"
    
    def detener(self):
        return "Reproducción detenida"
    
    def expulsar(self):
        return "DVD expulsado"

class Proyector:
    def encender(self):
        return "Proyector encendido"
    
    def apagar(self):
        return "Proyector apagado"
    
    def modo_pantalla_ancha(self):
        return "Proyector en modo pantalla ancha (16:9)"

class LucesTeatrales:
    def atenuar(self, nivel):
        return f"Luces atenuadas al {nivel}%"
    
    def encender(self):
        return "Luces encendidas"

class PantallaDeCine:
    def bajar(self):
        return "Pantalla bajada"
    
    def subir(self):
        return "Pantalla subida"

# Facade
class CineEnCasaFacade:
    def __init__(self):
        self.amplificador = Amplificador()
        self.dvd = ReproductorDVD()
        self.proyector = Proyector()
        self.luces = LucesTeatrales()
        self.pantalla = PantallaDeCine()
    
    def ver_pelicula(self, pelicula):
        print("Preparando el sistema de cine en casa para ver una película...")
        results = []
        results.append(self.pantalla.bajar())
        results.append(self.proyector.encender())
        results.append(self.amplificador.encender())
        results.append(self.amplificador.configurar_fuente("DVD"))
        results.append(self.amplificador.configurar_volumen(8))
        results.append(self.luces.atenuar(30))
        results.append(self.dvd.encender())
        results.append(self.dvd.reproducir(pelicula))
        
        return "\n".join(results)
    
    def terminar_pelicula(self):
        print("Apagando el sistema de cine en casa...")
        results = []
        results.append(self.dvd.detener())
        results.append(self.dvd.expulsar())
        results.append(self.dvd.apagar())
        results.append(self.amplificador.apagar())
        results.append(self.proyector.apagar())
        results.append(self.luces.encender())
        results.append(self.pantalla.subir())
        
        return "\n".join(results)

# Cliente
# Ahora el cliente solo necesita interactuar con la fachada
cine_en_casa = CineEnCasaFacade()

# Ver película con una simple llamada
print(cine_en_casa.ver_pelicula("El Padrino"))

print("\nTerminando la película:")
print(cine_en_casa.terminar_pelicula())