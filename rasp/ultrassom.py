#!/usr/bin/env python3

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

import sys
import pigpio
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

class Ultrassom:
    """ Classe para medir distância usando o sensor HC-04 """
    pino_trigger_ = 5
    pino_echo_ = 5
    tick_alto = 0
    tick_baixo = 0
    delta = 0
    distancia = 0
        
    def __init__(self, classe_pigpio, pino_trigger, pino_echo):
        self.pino_trigger_ = pino_trigger
        self.pino_echo_ = pino_echo 
        
        self.pigpio_local = classe_pigpio       
        
        self.pigpio_local.set_mode(self.pino_echo_, pigpio.INPUT)
        self.pigpio_local.set_mode(self.pino_trigger_, pigpio.OUTPUT)
        
        self.pigpio_local.set_glitch_filter(self.pino_echo_, 10)
        self.callback = self.pigpio_local.callback(self.pino_echo_,
                                                   pigpio.EITHER_EDGE, self.onChange)
        
        self.job = Job(interval=timedelta(seconds=0.3), execute=self.trigger_thread)
        
    def iniciar(self):
        self.job.start()
         
    def onChange(self, gpio, level, tick):
        
        if (level == 1):
            self.tick_alto = tick
        else:
            self.tick_baixo = tick
            
            self.delta = self.tick_baixo - self.tick_alto 
            
            # Em caso de overflow de tick
            if self.delta < 0:
                self.delta = 2**32 - self.tick_alto + self.tick_baixo
               
            # Distância em cm
            self.distancia = ((self.delta/10000)* 343) / 2
            
            #Debug 
            # print('l: ' + str(level) + '  ' + str(tick) + ' d: ' + str(self.delta) + ' ' +  str(self.distancia))        
                
    def obter(self):
        return self.distancia
    
    def trigger_thread(self):                
        self.pigpio_local.gpio_trigger(self.pino_trigger_, 10, 1)
    
    def parar(self):
        self.job.stop()
        self.callback.cancel()        