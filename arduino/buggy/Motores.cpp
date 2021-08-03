/*
  Motores.cpp - Biblioteca para controle de motores do Buggy 4x4.
  Created by Renan Augusto Starke, July 22, 2021.
  Released into the public domain.
*/

#include "Motores.h"

Motores::Motores()
{
  /* Configuração dos pinos */
  pinMode(M1, OUTPUT);
  pinMode(M1N, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(M2N, OUTPUT);
}

void Motores::parar()
{
  /* Desliga todos os motores */
  digitalWrite(M1, LOW);
  digitalWrite(M1N, LOW);
  digitalWrite(M2, LOW);
  digitalWrite(M2N, LOW);  
}


void Motores::frente(unsigned char velocidade){
  parar();

  /*digitalWrite(M1, HIGH);  
  digitalWrite(M2, HIGH); */
  velocidade &= 0xff;

  analogWrite(M1, velocidade);
  analogWrite(M2, velocidade);

}

void Motores::tras(unsigned char velocidade){
  parar();

  velocidade &= 0xff;
  /* digitalWrite(M1N, HIGH);
  digitalWrite(M2N, HIGH); */

  analogWrite(M1N, velocidade);
  analogWrite(M2N, velocidade);

}

void Motores::direita(unsigned char velocidade){
  parar();
  velocidade &= 0xff;
  
  /*digitalWrite(M1, HIGH);
  digitalWrite(M2N, HIGH);*/

  analogWrite(M1, velocidade);
  analogWrite(M2N, velocidade);

  
}

void Motores::esquerda(unsigned char velocidade){
  parar();
  velocidade &= 0xff;

  /* digitalWrite(M2N, HIGH);
  digitalWrite(M1, HIGH);  */

  analogWrite(M2, velocidade);
  analogWrite(M1N, velocidade);
}
