
#include "pitches.h"
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
}

void loop() {
  // no need to repeat the melody.
  if (Serial.available()){
    char serialListener = Serial.read();
  
  if (serialListener == 'f'){
    digitalWrite(22, 1);
    digitalWrite(23, 1);
    digitalWrite(22,0);
    digitalWrite(23,0);
    tone(BDPIN_BUZZER, NOTE_C4,500);
    delay(500);
    noTone(BDPIN_BUZZER);
    tone(BDPIN_BUZZER, NOTE_A4,500);
    delay(500);
    noTone(BDPIN_BUZZER);   
  }
  else if (serialListener == 'b'){
    digitalWrite(13,1);
    digitalWrite(24,1);
    digitalWrite(25,1);
    delay(1000);
    digitalWrite(13,0);
    digitalWrite(24,0);
    digitalWrite(25,0);
    delay(1000);   
  }
}
}
