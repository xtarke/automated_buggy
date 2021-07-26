/*
  Encoder.cpp - Biblioteca para mediação de velocidade usando encoder para buggy 4x4.
  Created by Renan Augusto Starke, July 26, 2021.
  Released into the public domain.
*/

#include "Encoder.h"

unsigned long Encoder::pulsos = 0;

Encoder::Encoder(unsigned char pino)
{
  /* Configuração dos pinos */
  pinMode(pino, INPUT);

  tempo = 0;
  
  /* Guarda informaçẽos dos pinos */
  _pino = pino;
  
  /* Contagem dos pulsos */  
  pulsos = 0;
  
  attachInterrupt(pino, Encoder::contador, FALLING);  
}

void Encoder::contador(){
    pulsos++;

     Serial.print('OI');
}

void Encoder::atualizar(){
  
  /* Mede a velocidade a cada 1000 ms */
  if (millis() - tempo >= 1000)
  {
    //Desabilita interrupcao durante o calculo
    detachInterrupt(_pino);
    
    /* velocidade = (60 * 1000 / pulsos_por_volta ) / (millis() - tempo) * pulsos; */
    //velocidade = pulsos / (millis() - tempo);
    
    tempo = millis();
    pulsos = 0;    

    attachInterrupt(_pino, Encoder::contador, FALLING);  
  }  
}

unsigned long Encoder::obter_velocidade(){
  return velocidade;
}

