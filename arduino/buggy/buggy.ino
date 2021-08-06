/*
  buggy.ino - Aplicação exemplo para o buggy 4x4
  
  - Exibe os dados dos sensores pelo terminal UART 9600 bps.
  - Recebe comandos da serial para movimentação dos motores.
  
  Created by Renan Augusto Starke, July 26, 2021.  
  Released into the public domain.
*/


#include "Motores.h"
#include "Ultrassom.h"
#include "Encoder.h"
#include "Baterias.h"
#include "Linha.h"

/* Tarefas básicas do exemplo */
void tarefa_1();
void tarefa_2();
volatile bool exibir_estado = true;

/* Instâncias das classe dos sensores/atuadores */
Motores motores;
Baterias baterias;
Linha seguidor_linha;
Ultrassom ultrassom_1(Ultrassom::ECHO1, Ultrassom::TRIG1);
Encoder encoder_0 (Encoder::D0);


/* Configuração e mensagem inicial */
void setup() {
  
  Serial.begin(9600);
  while (!Serial); 

  Serial.println("Teste buggy 4x4");
  Serial.println("f: mover para frente");
  Serial.println("r: mover para trás");
  Serial.println("e: mover para esquerda");
  Serial.println("d: mover para direita");  
  Serial.println("s: exibir estado dos sensores a cada 1s");
  Serial.println("i: exibir descrição das dos estados");

  delay(5000);  

}

/* Loop de atualização do sensores e das tarefas */
void loop() {
  
  encoder_0.atualizar();
  ultrassom_1.atualizar();

 
  tarefa_1();
  tarefa_2();
}

/* Tarefa 2: comandos da serial */
void tarefa_1(){

  /* Caso tenha recebido algum dado do PC */
  if (Serial.available()) {
     char dado_recebido = Serial.read();
     
      if (dado_recebido == 'p')
          motores.parar();          
      else if (dado_recebido == 'f')
          motores.frente(200);      
      else if (dado_recebido == 'r')
          motores.tras(200);      
      else if (dado_recebido == 'e')
          motores.esquerda(150);          
      else if (dado_recebido == 'd')
          motores.direita(150);
      else if (dado_recebido == 's') {
        if (exibir_estado == true)
          exibir_estado = false;
        else
          exibir_estado = true;        
      }
      
      if (dado_recebido == 'i') {
        Serial.println("Bat0\tBat1\tVelocidade\tDistância");
      }

  }
}

/* Exibe dados dos sensores */
void tarefa_2(){
  static unsigned long tempo_atual = 0;

  /* Escalonamento a cada 1s. Se ativado a exibição */
  if ((exibir_estado) && (millis() - tempo_atual >= 1000)){
    
    Serial.print(baterias.obter_bateria_0());
    Serial.print("\t");
    Serial.print(baterias.obter_bateria_1());
    Serial.print("\t");
    Serial.print(encoder_0.obter_velocidade());
    Serial.print("\t");
    Serial.print(ultrassom_1.obter_distancia());
    Serial.print("\t");
    Serial.print(seguidor_linha.obter_esquerda());
    Serial.print("\t");
    Serial.print(seguidor_linha.obter_direita());
    
    Serial.println("");
    
    tempo_atual = millis();    
  }  
}



