
#include "Motores.h"
#include "Ultrassom.h"



Motores mot;
Ultrassom sensor_1(Ultrassom::ECHO1, Ultrassom::TRIG1);


int teste = 0;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  while (!Serial); 

}

void loop() {
  // put your main code here, to run repeatedly:

  if (teste){
  
    mot.frente(150);
    delay(3000);     
  
    mot.tras(150);
    delay(3000); 

    mot.direita(150);
    delay(3000); 

    mot.esquerda(150);
    delay(3000); 

    teste = 0;
    mot.parar();
  }


  unsigned long dist = sensor_1.medir();


  delay(1000);


  Serial.println(dist);

  

}
