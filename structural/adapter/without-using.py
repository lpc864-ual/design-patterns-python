# Sin patrón Adapter
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

# Cliente
def controlar_motor(motor):
    # El cliente espera una interfaz de tipo MotorGasolina
    print(motor.encender())
    print(motor.acelerar())
    print(motor.detener())

# Esto funciona bien con el motor de gasolina
motor_gasolina = MotorGasolina()
controlar_motor(motor_gasolina)

# Pero esto fallará con un motor eléctrico
# motor_electrico = MotorElectrico()
# controlar_motor(motor_electrico)  # Error: no tiene método encender()