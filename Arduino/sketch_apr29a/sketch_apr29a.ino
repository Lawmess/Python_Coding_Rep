#include <SPI.h>

volatile byte receivedData;
boolean newData = false;

void setup() {
  Serial.begin(9600); 
  pinMode(MISO, OUTPUT);
  // Initialize SPI
  SPCR |= _BV(SPE);
  // Enable SPI interrupt
  SPCR |= _BV(SPIE);
}

// SPI interrupt routine
ISR(SPI_STC_vect) {
  receivedData = SPDR; 
  newData = true;
}

void loop() {
  if (newData == true) {
    Serial.print("Received: ");
    Serial.println(receivedData);
    newData = false;
  }
}
