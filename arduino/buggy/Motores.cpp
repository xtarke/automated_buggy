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


void Motores::frente(){
  parar();

  digitalWrite(M1, HIGH);
  digitalWrite(M2, HIGH);  
}

void Motores::tras(){
  parar();

  digitalWrite(M1N, HIGH);
  digitalWrite(M2N, HIGH);
}

void Motores::esquerda(){
  parar();

  digitalWrite(M1, HIGH);
  digitalWrite(M2N, HIGH);
}

void Motores::direita(){
  parar();

  digitalWrite(M2N, HIGH);
  digitalWrite(M1, HIGH);  
}
