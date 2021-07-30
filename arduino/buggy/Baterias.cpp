/*
  Baterias.cpp - Biblioteca para medição das baterias para buggy 4x4.
  
  Canal/Pino ADC0 (Pino A2) (Ganho = 1/3) é a soma de ambas baterias e 
  canal/Pino ADC1 (Pino A1) (Ganho = 2/3) é bateria inferior
    - Bateria 0: Canal 0 - Canal 1   
    - Bateria 1: Canal 1  
  
  Created by Renan Augusto Starke, July 26, 2021.  
  Released into the public domain.
*/

#include "Baterias.h"

/* Cabeçalhos e vetores de interrupções: código low level para o ADC */
#include <avr/io.h>
#include <avr/interrupt.h>

/* Variáveis para filtro */
static volatile unsigned long valor_baterias[2][8] = {0};
static volatile unsigned long sum_bat0 = 0;
static volatile unsigned long sum_bat1 = 0;

Baterias::Baterias()
{
  /* Configuração do AD */

  /* Ref externa no pino AVCC com capacitor de 100n em VREF.
   * Habiltiação apenas no Canal 0 */
  ADMUX = 1 << REFS0;
  /* Reset canais */
  ADMUX &= ~0x0f;
  /* Bat */
  ADMUX |= 0x01;
  
  /* Habilita AD:
   * Conversão contínua
   * IRQ ativo
   * Prescaler de 128 */
  ADCSRA = (1 << ADEN)  |                               //ADC Enable
          (1 << ADSC)   |                               // ADC Start conversion
          (1 <<  ADATE) |                               // ADC Auto Trigger
          (1 << ADPS0)  | (1 << ADPS1) | (1 << ADPS2) | //ADPS[0..2] AD Prescaler selection
          (1 << ADIE);    //AD IRQ ENABLE

  /* Auto trigger no overflow do Timer0 (Configurado pelo Arduino) */
  ADCSRB = (1<< ADTS2);
}

unsigned long Baterias::obter_bateria_0(){
  
  unsigned long data = sum_bat0 >> 3;
  
  /*   10  V = 5 * ADC
   *  ----    -------
   *   33         1024 
   *
   *     V = 1650 * ADCC   ( *100 para escala em deciVolt) 
   *         ------------
   *             2048 
   */
  
  
  unsigned long volts = (1650 * data)  >> 10;

  return volts - obter_bateria_1();
}

unsigned long Baterias::obter_bateria_1(){
  
  unsigned long data = sum_bat1 >> 3;

  /*  2 V = 5 * ADC
   *  ----    -------
   *   3         1024 
   *
   *     V = 15 * ADCC  ( *100 para escala em deciVolt) 
   *         --------
   *           2048 
   */
  
  unsigned long volts = (1500 * data)  >> 11;

  return volts;
}


ISR(ADC_vect)
{
  /* Lê o valor do conversor AD na interrupção:
   * ADC é de 10 bits, logo valor_adc deve ser
   * de 16 bits
   */
  static unsigned char canal = Baterias::Bateria_1;
  static unsigned char i = 0;
  static unsigned char j = 0;
  unsigned long valor_ADC = ADC;

  if (canal == Baterias::Bateria_1) {  
    sum_bat0 -=  valor_baterias[0][i];
    valor_baterias[0][i] = valor_ADC;
    sum_bat0 += valor_ADC;
    i++;
    i = i & 0x7;
  }
  else {
    sum_bat1 -=  valor_baterias[1][j];
    valor_baterias[1][j] = valor_ADC;
    sum_bat1 += valor_ADC;
    j++;
    j = j & 0x7;    
  }

  /* Multiplexão dos canais */
  ADMUX &= ~0x0f;  
  ADMUX |= canal;
  canal++;

  if (canal > Baterias::Bateria_0)
    canal = Baterias::Bateria_1; 
}



