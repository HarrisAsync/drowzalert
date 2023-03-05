#include <SoftwareSerial.h>

#define SHOCK_PIN 12
#define ARD_TX_BT_RX 6
#define ARD_RX_BT_TX 7

SoftwareSerial BTserial(ARD_RX_BT_TX, ARD_TX_BT_RX); // ARD RX, ARD TX

void setup() {
  BTserial.begin(9600);

  pinMode(SHOCK_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(SHOCK_PIN, LOW);
  digitalWrite(LED_BUILTIN, LOW);
  delay(3000);
}

void loop() {
  if (BTserial.available() > 0) 
  {
      BTserial.read();
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(SHOCK_PIN, HIGH);
      delay(800);
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(SHOCK_PIN, LOW);
      delay(3000);
  }
}
