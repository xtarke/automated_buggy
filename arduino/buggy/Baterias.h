/*
  Baterias.h - Biblioteca para medição das baterias para buggy 4x4.
  Created by Renan Augusto Starke, July 30, 2021.
  Released into the public domain.
*/
#ifndef BATERIAS_H
#define BATERIAS_H

#include "Arduino.h"

class Baterias
{
  public:
    //static volatile unsigned long valor_baterias[2];
        
    Baterias();
    
    unsigned long obter_bateria_0();
    unsigned long obter_bateria_1();

    enum CANAIS { Bateria_1 = 1, Bateria_0 = 2};
    
  private:    
    
};

#endif
