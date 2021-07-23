/*
  Ultrassom.h - Biblioteca para mediação de distância usando HC-motores do Buggy 4x4.
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

    unsigned long medir();

    enum SENSOR_0 { ECHO0 = 8, TRIG0 = 7};
    enum SENSOR_1 { ECHO1 = 2, TRIG1 = 4};
    
  private:    
    unsigned char _echo_pin;
    unsigned char _trigger_pin;    
       
    unsigned long distancia;

};

#endif
