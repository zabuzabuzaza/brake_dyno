const int analogIn = A0;  // Analog input pin that the potentiometer is attached to
const int digitalOut = 13; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);

  digitalWrite(LED_BUILTIN, LOW);  
  digitalWrite(digitalOut, LOW);  
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogIn);
  // map it to the range of the analog out:
  // inputValue = map(sensorValue, 0, 1023, 0, 255);
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);
  
  // print the results to the Serial Monitor:
  Serial.print(sensorValue);
  Serial.print('\n'); 


  if (Serial.available()){
    int inByte = Serial.read(); 
    if (inByte == '1') {
      digitalWrite(digitalOut, HIGH); 
    } 
    else {
      digitalWrite(digitalOut, LOW);  
    }
  }
  
  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(2);
}
