#include <Pushbutton.h>
#include <Encoder.h>

Encoder knob(2, 3);
Pushbutton button(7);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  Serial.println("Encoder Test:");
}

long knobposition = -999;
long IPRGM_Pos = -999;
long EPRGM_Pos = -999;
bool PRGM = true;
int PRGM_Pin = 5;
long EMONTR_new = 0;
long IMONTR_new = 0;
long EMONTR = 0;
long IMONTR = 0;


void loop() {
  EMONTR_new = analogRead(A5);
  EMONTR_new = 5*EMONTR_new/1023;
  IMONTR_new = analogRead(A4);
  IMONTR_new = 5*IMONTR_new/1023;
  if (abs(EMONTR_new-EMONTR) > 5 || abs(IMONTR_new-IMONTR) > 5){
    EMONTR = EMONTR_new;
    IMONTR = IMONTR_new;
    Serial.print("E MONTR: ");
    Serial.print(EMONTR);
    Serial.println();
    Serial.print("I MONTR: ");
    Serial.print(IMONTR);
    Serial.println();
  }
  long newpos;
  if(button.getSingleDebouncedPress()){
    PRGM = !PRGM;
    if (PRGM){
      IPRGM_Pos = knobposition;
      knobposition = EPRGM_Pos;
      knob.write(knobposition);
      PRGM_Pin = 5;
    }
    else{
      EPRGM_Pos = knobposition;
      knobposition = IPRGM_Pos;
      knob.write(knobposition);
      PRGM_Pin = 6;
    }
    Serial.print("Button Pressed");
    Serial.print(PRGM);
    Serial.println();
    
  }
  newpos = knob.read();
  if (newpos >= 255)
  {
    newpos = 255;
    knob.write(255);
  }
  if (newpos <= 0)
  {
    newpos = 0;
    knob.write(0);
  } 
  if (newpos != knobposition) {
    Serial.print("Position = ");
    Serial.print(newpos);
    Serial.println();
    analogWrite(PRGM_Pin,newpos);
    knobposition = newpos;
  }

  // if a character is sent from the serial monitor,
  // reset both back to zero.
  if (Serial.available()) {
    Serial.read();
    Serial.println("Reset knob to zero");
    knob.write(0);
  }
}