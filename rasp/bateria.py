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
import threading, time
from datetime import timedelta

class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
        self.stopped.set()
        self.join()
    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)

class Bateria:
    """Classe para monitorar as baterias. Utiliza o módulo ADS115 conectado
    no barramento I2C-1 do Raspberry Pi: /dev/i2c-1
    Canal 0 (Ganho = 1/3) é a soma de ambas baterias e canal 1 (Ganho = 2/3) é bateria inferior
    - Bateria 1: Canal 0 - Canal 1   
    - Bateria 2: Canal 1
    """
    
    ganho_pot_0 = float(1/3)
    ganho_pot_1= float(2/3)
    
    ads115_configs = {'addr' : 0x48, 
                      'data_reg': 0x00, 
                      'config_reg': 0x01,              
                      'cha_00': 0x83C3, 
                      'cha_01': 0x83D3 }
    
    """ Registrador de configuração (16 bits):
    Leitura do canal 0: 0x83C3
    Leitura do canal 1: 0x83D3
    
    - Single shot
    - FSR = 4.096 / 2 (+ ou -)
    - ADC = Vin * 2**16   (sem ganho da placa de potência)
            -----------
             4.096 * 2 
    """
    
    def __init__(self, pinos):
        
        self.pinos = pinos
        self.bateria_1 = 0
        self.bateria_2 = 0
        self.adc = pinos.i2c_open(1, self.ads115_configs['addr'])        
        self.job = Job(interval=timedelta(seconds=0.5), execute=self.ler_baterias)
        
    def iniciar(self):
        self.job.start()
        
    def parar(self):
        self.job.stop()
        
    def obter(self, n):
        if n == 1:
            return self.bateria_1
        else:
            return self.bateria_2        
          
    def ler_baterias(self):
        self.ler_canal_0()
        self.ler_canal_1()
                          
        self.bateria_2 = self.canal_1 * 4.096 * 2 / (2**16) / self.ganho_pot_1     
        self.bateria_1 = self.canal_0 * 4.096 * 2 / (2**16) / self.ganho_pot_0 - self.bateria_2
       
        # print("{:>5.3f}\t{:>5.3f}".format(self.bateria_1, self.bateria_2))
        
    def ler_canal_0(self):
        self.pinos.i2c_write_word_data(self.adc, self.ads115_configs['config_reg'],
                                       self.ads115_configs['cha_00'])     
        read = self.pinos.i2c_read_word_data(self.adc,
                                             self.ads115_configs['data_reg'])        
        
        self.canal_0 = ((read >> 8) & 0xff00) | ((read << 8) & 0xff00)        
               
    def ler_canal_1(self):
        self.pinos.i2c_write_word_data(self.adc, self.ads115_configs['config_reg'],
                                       self.ads115_configs['cha_01'])     
        read = self.pinos.i2c_read_word_data(self.adc,
                                             self.ads115_configs['data_reg'])        
        
        self.canal_1 = ((read >> 8) & 0xff00) | ((read << 8) & 0xff00)   
       
