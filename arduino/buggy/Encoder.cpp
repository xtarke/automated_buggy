/*
  Encoder.cpp - Biblioteca para mediação de velocidade usando encoder para buggy 4x4.
  Created by Renan Augusto Starke, July 26, 2021.
  Released into the public domain.
*/

#include "Encoder.h"

/* Cabeçalhos e vetores de interrupções: código low level para PCINTs */
#include <avr/io.h>
#include <avr/interrupt.h>

volatile unsigned long Encoder::pulsos_d0 = 0;
volatile unsigned long Encoder::pulsos_d1 = 0;

Encoder::Encoder(unsigned char pino)
{
  /* Configuração dos pinos */
  pinMode(pino, INPUT);

  tempo = 0;
  
  /* Guarda informaçẽos dos pinos */
  _pino = pino;
  
  /* Contagem dos pulsos */  
  pulsos_d0 = 0;
  pulsos_d1 = 0;

  /* attachInterrupt: implementado apenas para IRQ externa 0 e 1 
   * attachInterrupt(pino, Encoder::contador, FALLING);  
   *
   *  Pinos D0 e D1 estão mapeados em PCINT4(PB4) e PCINT5 (PB5)   */
  if (pino == Encoder::D0)
    PCMSK0 |= (1 << PCINT5);
  else
    PCMSK0 |= (1 << PCINT4);
   
  PCICR |= 1 << PCIE0;  
}

/* PCINT deve-se testar qual pino gerou a IRQ */
ISR(PCINT0_vect)
{
  /* Teste para D0 */
  if (PINB & (1 << PB5)){
    Encoder::pulsos_d0++;    
  }

  /* Teste para D1 */
  if (PINB & (1 << PB4))
    Encoder::pulsos_d1++;



}

void Encoder::atualizar(){
  unsigned long pulsos = 0;
  
  /* Mede a velocidade a cada 500 ms */
  if (millis() - tempo >= 500)
  {
    /* Desabilita interrupcao durante o calculo */       
    if (_pino == Encoder::D0){
      /* Desabilita interrupcao durante o calculo */
      PCMSK0 &= ~(1 << PCINT5);
      pulsos = pulsos_d0;
      pulsos_d0 = 0;
    }
    else {
      PCMSK0 &= ~(1 << PCINT4);
      pulsos = pulsos_d1;
      pulsos_d1 = 0;
    }
      
    /* velocidade = (60 * 1000 / pulsos_por_volta ) / (millis() - tempo) * pulsos; */
    velocidade = pulsos << 2;          //Rever: usar 500ms para multipliar por 2
    tempo = millis();

    if (_pino == Encoder::D0)
      PCMSK0 |= (1 << PCINT5);
    else
      PCMSK0 |= (1 << PCINT4);    
  }  
}

unsigned long Encoder::obter_velocidade(){
  return velocidade;
}
