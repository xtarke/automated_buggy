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
import time

class Sensor_linha:
    """ Classe para detectar e seguir uma linha através de um sensor óptico
    na frente do carrinho
    """
    pino_ = 5
    estado = 0
        
    def __init__(self, classe_pigpio, pino):
        self.pino_ = pino       
        self.pigpio_local = classe_pigpio       
        
        self.pigpio_local.set_mode(self.pino_, pigpio.INPUT)
        self.pigpio_local.set_glitch_filter(self.pino_, 1000)
        self.callback = self.pigpio_local.callback(self.pino_,
                                                   pigpio.EITHER_EDGE, self.onChange)
         
    def onChange(self, gpio,level,tick):
        estado = level        
        #debug
        #print(estado)
        
    def ler(self):
        return estado
    
    def parar(self):        
        self.callback.cancel()