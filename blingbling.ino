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
    
      digitalWrite(ledpin, HIGH);  // turn ON the LED
      digitalWrite(11, HIGH);
      digitalWrite(9, HIGH);
      digitalWrite(7, HIGH);
      delay(100);  
   
      digitalWrite(ledpin, LOW);  // turn ON the LED
      digitalWrite(11, LOW);
      digitalWrite(9, LOW);
      digitalWrite(7, LOW);
   
   
    val = Serial.read();         // read it and store it in 'val'
    Serial.write(val);
  }/*
  */
  delay(100);                    // wait 100ms for next reading
}

