/*
  Melody

  Plays a melody

  circuit:
  - 8 ohm speaker on digital pin 8

  created 21 Jan 2010
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody
*/

#include "pitches.h"

void setup() {
  // put your setup code here, to run once:
  
}

void loop() {
  // no need to repeat the melody.
  tone(BDPIN_BUZZER, NOTE_C4, 500);
  delay(500);
  noTone(BDPIN_BUZZER);
  tone(BDPIN_BUZZER, NOTE_G3, 500);
  delay(500);
  noTone(BDPIN_BUZZER);
  tone(BDPIN_BUZZER, NOTE_A3, 500);
  delay(500);
  noTone(BDPIN_BUZZER);
  tone(BDPIN_BUZZER, NOTE_B3, 500);
  delay(500);
  noTone(BDPIN_BUZZER);
}
