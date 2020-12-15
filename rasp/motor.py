import pigpio
import time

class Motor:
    """Classe para controlar os motores do buggy"""
    
    M1 = 18
    M2 = 13
    M1N = 12
    M2N = 19
    
    def __init__(self, pinos):
        
        # Inicializacao dos pinos 
        pinos.set_mode(self.M1, pigpio.OUTPUT)
        pinos.set_mode(self.M2, pigpio.OUTPUT)
        pinos.set_mode(self.M1N, pigpio.OUTPUT)
        pinos.set_mode(self.M2N, pigpio.OUTPUT)
        
        # Todos desligados
        pinos.write(self.M1, 0)
        pinos.write(self.M2, 0)
        pinos.write(self.M1N, 0)
        pinos.write(self.M2N, 0)
