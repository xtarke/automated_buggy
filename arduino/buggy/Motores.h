/*
  Motores.h - Biblioteca para controle de motores do Buggy 4x4.
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/
#ifndef MOTORES_H
#define MOTORES_H

#include "Arduino.h"

class Motores
{
  public:
    Motores();
    
    void frente();
    void tras();
    void esquerda();
    void direita();
    void parar();
    
  private:
    enum pins {M1 = 6, M1N = 5, M2 = 11, M2N = 3};
};

#endif
