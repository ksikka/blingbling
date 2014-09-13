#include <TimedAction.h>

char val; // variable to receive data from the serial port
int ledpin = 13;
boolean isOn = false;

void setup() {
  pinMode(ledpin, OUTPUT);  // pin 48 (on-board LED) as OUTPUT
  Serial.begin(9600);       // gstart serial communication at 9600bps
}


void loop() {
  if( Serial.available() )       // if data is available to read
  {
    if (isOn) {
      digitalWrite(ledpin, LOW);  // turn ON the LED
      isOn = false;
    } else {
      digitalWrite(ledpin, HIGH);  // turn ON the LED
      isOn = true;
    }
    val = Serial.read();         // read it and store it in 'val'
    Serial.write(val);
  }/*
  if( val == 'H' )               // if 'H' was received
  {
    digitalWrite(ledpin, HIGH);  // turn ON the LED
  } 
  else { 
    digitalWrite(ledpin, LOW);   // otherwise turn it OFF
  }
  */
  delay(100);                    // wait 100ms for next reading
}

