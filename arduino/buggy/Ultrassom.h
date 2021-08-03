/*
  Ultrassom.h - Biblioteca para medição de distância usando HC-SR04 para buggy 4x4.
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/
#ifndef ULTRASSOM_H
#define ULTRASSOM_H

#include "Arduino.h"

class Ultrassom
{
  public:
    Ultrassom(unsigned char echo_pin, unsigned char trigger_pin);

    void atualizar();
    unsigned long obter_distancia();

    enum SENSOR_0 { ECHO0 = 8, TRIG0 = 7};
    enum SENSOR_1 { ECHO1 = 2, TRIG1 = 4};
    
  private:    
    unsigned long medir();
    
    unsigned char _echo_pin;
    unsigned char _trigger_pin;    
       
    unsigned long distancia;
    unsigned long tempo;

};

#endif
