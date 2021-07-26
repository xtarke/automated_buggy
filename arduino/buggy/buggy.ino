
#include "Motores.h"
#include "Ultrassom.h"
#include "Encoder.h"



Motores mot;
//Ultrassom sensor_1(Ultrassom::ECHO1, Ultrassom::TRIG1);
Encoder enc_1 (Encoder::D0);


int teste = 0;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  while (!Serial); 

  //mot.frente(170);

}

void loop() {
  // put your main code here, to run repeatedly:

  static unsigned long timeold = 0;
  //

//  if (teste){
//  
//    mot.frente(150);
//    delay(3000);     
//  
//    mot.tras(150);
//    delay(3000); 
//
//    mot.direita(150);
//    delay(3000); 
//
//    mot.esquerda(150);
//    delay(3000); 
//
//    teste = 0;
//    mot.parar();
//  }

  enc_1.atualizar();


  if (millis() - timeold >= 1000){
    Serial.println(enc_1.obter_velocidade());
    timeold = millis();
  }


  //unsigned long dist = sensor_1.medir();
  

  //delay(1000);


  

  

}
