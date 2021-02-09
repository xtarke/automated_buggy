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
import RPi.GPIO as GPIO
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
    
    def __init__(self, pino):        
        self.pino_encoder = pino
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pino_encoder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.pino_encoder, GPIO.FALLING, 
            callback=self.callback_pulsos, bouncetime=15)
        
        self.job = Job(interval=timedelta(seconds=1), execute=self.velocidade_thread)
        
    
    def velocidade_thread(self):
        
        # print(self.pulsos)
        
        self.velocidade = self.pulsos - self.delta        
        self.delta = self.pulsos        
        self.velocidade = self.velocidade 
        
        print(self.velocidade)
        
        
    def iniciar(self):
        self.job.start()
    
    def parar(self):
        self.job.stop()
        GPIO.cleanup()

    def callback_pulsos(self, channel):
        self.pulsos = self.pulsos + 1
    
#
#def signal_handler(sig, frame):
#    GPIO.cleanup()
#    sys.exit(0)
#
#def button_pressed_callback(channel):
#    print("Pulse detected!")
#
#if __name__ == '__main__':
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
#    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
#            callback=button_pressed_callback, bouncetime=100)
#    
#    signal.signal(signal.SIGINT, signal_handler)
#    signal.pause()