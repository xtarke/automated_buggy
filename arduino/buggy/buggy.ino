
#include "Motores.h"
#include "Ultrassom.h"
#include "Encoder.h"
#include "Baterias.h"



Motores mot;
Ultrassom sensor_1(Ultrassom::ECHO1, Ultrassom::TRIG1);
Encoder enc_0 (Encoder::D0);

Baterias bats;

int teste = 0;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  while (!Serial); 

 // mot.frente(170);

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

  //enc_0.atualizar();


  if (millis() - timeold >= 1000){
    //Serial.println(enc_0.obter_velocidade());
    timeold = millis();

    Serial.println(bats.obter_bateria_0());
    Serial.println(bats.obter_bateria_1());
    
  }


  //unsigned long dist = sensor_1.medir();
  

  //delay(1000);


  

  

}
