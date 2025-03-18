# Con patrón Adapter
class MotorGasolina:
    def encender(self):
        return "Motor de gasolina encendido"
    
    def acelerar(self):
        return "Acelerando motor de gasolina"
    
    def detener(self):
        return "Motor de gasolina detenido"

class MotorElectrico:
    def conectar(self):
        return "Motor eléctrico conectado"
    
    def activar(self):
        return "Motor eléctrico activado"
    
    def mover(self):
        return "Moviendo motor eléctrico"
    
    def desconectar(self):
        return "Motor eléctrico desconectado"

# Adaptador que convierte la interfaz del motor eléctrico a la interfaz del motor de gasolina
class AdaptadorMotorElectrico:
    def __init__(self, motor_electrico):
        self.motor_electrico = motor_electrico
    
    # Implementa la interfaz que el cliente espera
    def encender(self):
        return self.motor_electrico.conectar() + " y " + self.motor_electrico.activar()
    
    def acelerar(self):
        return self.motor_electrico.mover()
    
    def detener(self):
        return self.motor_electrico.desconectar()

# Cliente
def controlar_motor(motor):
    # El cliente usa una interfaz común
    print(motor.encender())
    print(motor.acelerar())
    print(motor.detener())

# Esto funciona con motor de gasolina directamente
motor_gasolina = MotorGasolina()
print("Usando motor de gasolina:")
controlar_motor(motor_gasolina)

# Y ahora también funciona con el motor eléctrico a través del adaptador
motor_electrico = MotorElectrico()
adaptador = AdaptadorMotorElectrico(motor_electrico)
print("\nUsando motor eléctrico con adaptador:")
controlar_motor(adaptador)