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

# See:
# https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/

import sys
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

class Encoder:
    """ Classe para medir a velocidade utilizando o encoder óptico do carrinho
    Retorna a velocidade em pulso por segundo
    """

    pino_encoder = 5
    pulsos = 0
    delta = 0
    velocidade = 0
    
    def __init__(self, classe_pigpio, pino):
        self.pino_encoder = pino       
        self.pigpio_local = classe_pigpio       
        
        self.pigpio_local.set_mode(self.pino_encoder, pigpio.INPUT)
        self.callback = self.pigpio_local.callback(self.pino_encoder,
                                                   pigpio.RISING_EDGE, self.callback_pulsos)
        
        self.job = Job(interval=timedelta(seconds=0.5), execute=self.velocidade_thread)
        
    def velocidade_thread(self):
        
        self.velocidade = self.pulsos - self.delta        
        self.delta = self.pulsos        
        self.velocidade = self.velocidade * 2
        
        print(self.velocidade)
         
    def iniciar(self):
        self.job.start()
    
    def parar(self):
        self.job.stop()

    def callback_pulsos(self, gpio,level,tick):
        self.pulsos = self.pulsos + 1
    