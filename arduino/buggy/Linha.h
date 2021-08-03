/*
  Linha.h - Biblioteca para detectar/seguir uma linha para o buggy 4x4.
  Retorna a ...
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/
#ifndef LINHA_H
#define LINHA_H

#include "Arduino.h"

class Linha
{
  public:
    enum LINHA_PINOS {R_TCRT = A4, L_TCRT = A5};
    static const unsigned int amostras_filto = 100;
    volatile static unsigned char esquerda;
    volatile static unsigned char direita;
            
    Linha();
    unsigned char obter_esquerda();
    unsigned char obter_direita();
    
  private:
    
};

#endif