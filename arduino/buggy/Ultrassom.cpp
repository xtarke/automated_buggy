/*
  Ultrassom.h - Biblioteca para mediação de distância usando HC-motores do Buggy 4x4.
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/

#include "Ultrassom.h"

Ultrassom::Ultrassom(unsigned char echo_pin, unsigned char trigger_pin)
{
  /* Configuração dos pinos */
  pinMode(echo_pin, INPUT);
  pinMode(trigger_pin, OUTPUT); 
  digitalWrite(trigger_pin, LOW);

  /* Guarda informaçẽos dos pinos */
  _echo_pin = echo_pin;
  _trigger_pin = trigger_pin;
}

unsigned long Ultrassom::medir(){

  digitalWrite(_trigger_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(_trigger_pin, LOW);

  distancia = pulseIn(_echo_pin, HIGH);

  return distancia;
}

