/*
  Linha.cpp - Biblioteca para detectar/seguir uma linha para o buggy 4x4.
  Retorna a verdadeiro ou falso de acordo com a detecção.
  Essa biblioteca utiliza o overflow do Timer 2 para o filtro do sensor.
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/

#include "Linha.h"

/* Cabeçalhos e vetores de interrupções: código low level para PCINTs */
#include <avr/io.h>
#include <avr/interrupt.h>

#define CPL_BIT(y,bit) 	(y^=(1<<bit))

volatile unsigned char Linha::esquerda = 0;
volatile unsigned char Linha::direita = 0;

Linha::Linha()
{
  /* Configuração dos pinos */
  pinMode(R_TCRT, INPUT);
  pinMode(L_TCRT, INPUT);

//   pinMode(13, OUTPUT);

  /* Filtro do sensor óptico é feito por
   * counting debouncer no overflow do timer 2

   * Habilita IRQ de overflow. Configuração do timer é
   * realizada pelo Arduino.   */
  TIMSK2 = 1 << TOIE2;
}

/* Interrupção de overflow do Timer2 do AVR.
 * O Timer 2 é configurado pelo Arduino no modo PWM. 
 * Essa interrupção executa a cada 4ms aproximadamente */
ISR(TIMER2_OVF_vect){

  static unsigned int amostras_r = Linha::amostras_filto;
  static unsigned int amostras_l = Linha::amostras_filto;

  /* Debug: Piscar quando executar a ISR */
  CPL_BIT(PORTB, PB5);

  /* Se detectado borda de descida */
  if (digitalRead(Linha::R_TCRT))  {
      /* Se contagem = 0, debounce terminado */
      if (!(--amostras_r)) {
        Linha::direita = 1;
      }
  }
  else{
      Linha::direita = 0;
      amostras_r = Linha::amostras_filto;
  }

	/* Se detectado borda de descida */
  if (digitalRead(Linha::L_TCRT))  {
      /* Se contagem = 0, debounce terminado */
      if (!(--amostras_l)) {
        Linha::esquerda = 1;
      }
  }
  else{
      Linha::esquerda = 0;
      amostras_l = Linha::amostras_filto;
  }
}

unsigned char Linha::obter_esquerda(){
  return Linha::esquerda;
}
unsigned char Linha::obter_direita(){
  return Linha::direita;
}
