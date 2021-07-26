/*
  Encoder.h - Biblioteca para mediação de velocidade usando encoder para buggy 4x4.
  Created by Renan Augusto Starke, July 26, 2021.
  Released into the public domain.
*/
#ifndef ENCODER_H
#define ENCODER_H

#include "Arduino.h"

class Encoder
{
  public:
    static unsigned long pulsos;
    
    Encoder(unsigned char pino);
    unsigned long obter_velocidade();
    void atualizar();    

    enum SENSORES { D0 = 13, D1 = 12};
    
  private:    
    unsigned char _pino;          
    unsigned long velocidade;    
    unsigned long tempo;

    static void contador();
    
    

};

#endif
