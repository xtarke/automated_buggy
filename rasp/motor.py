# Copyright (c) 2020 Instituto Federal de Santa Catarina
# Author: Renan Augusto Starke
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import pigpio
import time
import bateria

class Motor:
    """Classe para controlar os motores do buggy"""
    
    # Pinos do PWM
    M1 = 18
    M2 = 13
    M1N = 12
    M2N = 19
       
    # Frequencia PWM
    pwm_freq = 1000
    
    def __init__(self, pinos):
        
        # Instância pigpio 
        self.pinos = pinos
        
        # Inicializacao dos pinos 
        pinos.set_mode(self.M1, pigpio.OUTPUT)
        pinos.set_mode(self.M2, pigpio.OUTPUT)
        pinos.set_mode(self.M1N, pigpio.OUTPUT)
        pinos.set_mode(self.M2N, pigpio.OUTPUT)
        
        self.parar()
        
    def parar(self):        
        # Todos desligados
        self.pinos.write(self.M1, 0)
        self.pinos.write(self.M2, 0)
        self.pinos.write(self.M1N, 0)
        self.pinos.write(self.M2N, 0)
        
    def mover_frente(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            razao_hardware = porcentagem/100. * 1000000
            
            self.pinos.hardware_PWM(self.M1, self.pwm_freq, int(razao_hardware))
            self.pinos.hardware_PWM(self.M2, self.pwm_freq, int(razao_hardware))
        
    def mover_re(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            razao_hardware = porcentagem/100. * 1000000
            
            self.pinos.hardware_PWM(self.M1N, self.pwm_freq, int(razao_hardware))
            self.pinos.hardware_PWM(self.M2N, self.pwm_freq, int(razao_hardware))
        
    def mover_esquerda(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            razao_hardware = porcentagem/100. * 1000000
            
            self.pinos.hardware_PWM(self.M1, self.pwm_freq, int(razao_hardware))
            self.pinos.hardware_PWM(self.M2N, self.pwm_freq, int(razao_hardware))  
        
    def mover_direita(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            razao_hardware = porcentagem/100. * 1000000
            
            self.pinos.hardware_PWM(self.M1N, self.pwm_freq, int(razao_hardware))
            self.pinos.hardware_PWM(self.M2, self.pwm_freq, int(razao_hardware))