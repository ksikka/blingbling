

char val; // variable to receive data from the serial port
int ledpin = 8;

void setup() {
  pinMode(13, OUTPUT);  // pin 48 (on-board LED) as OUTPUT
  pinMode(ledpin, OUTPUT);  // pin 48 (on-board LED) as OUTPUT
  Serial.begin(9600);       // start serial communication at 9600bps
}


void loop() {
  digitalWrite(13, HIGH);  // turn ON the LED
  if( Serial.available() )       // if data is available to read
  {
    val = Serial.read();         // read it and store it in 'val'
  }
  if( val == 'H' )               // if 'H' was received
  {
    digitalWrite(ledpin, HIGH);  // turn ON the LED
        digitalWrite(13, HIGH);  // turn ON the LED
  } else { 
    digitalWrite(ledpin, LOW);   // otherwise turn it OFF
  }
  delay(100);                    // wait 100ms for next reading
}
