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
import motor
import bateria


def main():
    print('Hello!')
    print('Digite a direção: ')
    print('p: parar')
    print('r: ré')
    print('e: esquerda')
    print('p: direita')
    print('q: sair')
        
    pinos = pigpio.pi()
    
    motores = motor.Motor(pinos)
    baterias = bateria.Bateria(pinos)
    
    
    dir = 's'
    
    while (dir != 'q'):
        
        # dir = input()
        
        if dir == 'p':
            motores.parar()
            
        if dir == 'f':
            motores.mover_frente(75)
        
        if dir == 'r':
            motores.mover_re(75)
        
        if dir == 'e':
            motores.mover_esquerda(75)
            
        if dir == 'd':
            motores.mover_direita(75)
            
            
        baterias.ler_baterias()
        
        print("{:>5.3f}\t{:>5.3f}".format(baterias.bateria_1, baterias.bateria_2))
        
        time.sleep(1)
        
    
    motores.parar()
    print('Bye Bye!')    

if __name__ == '__main__':
    main()


