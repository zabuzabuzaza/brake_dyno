#include <Servo.h> 

// input pins and values
int analogX = A0; 
int analogY = A1; 
int k_tc1 = 3; 
int k_tc2 = 4; 
int k_tc3 = 5; 

int inputX; 
int inputY; 
int inputTC1;
int inputTC2;
int inputTC3;

// output pins and values
Servo servo; 

int servoPin = 3; 
int servoAngle = 0; 


void setup() {
  Serial.begin(9600); 
  digitalWrite(LED_BUILTIN, LOW); 
  
  //Declaring LED pin as output
  pinMode(k_tc1, INPUT);
  pinMode(k_tc2, INPUT);
  pinMode(k_tc3, INPUT);

  servo.attach(servoPin); 
  pinMode(servoPin, OUTPUT);

}
void loop() {
  //Reading from potentiometer
  inputX = analogRead(analogX);
  inputY = analogRead(analogY);
  inputTC1 = digitalRead(k_tc1); 
  inputTC2 = digitalRead(k_tc2); 
  inputTC3 = digitalRead(k_tc3); 

  Serial.print(inputX); 
  Serial.print(','); 
  Serial.print(inputY); 
  Serial.print(','); 
  Serial.print(inputTC1); 
  Serial.print(','); 
  Serial.print(inputTC2); 
  Serial.print(','); 
  Serial.print(inputTC3); 
  Serial.print('\n'); 

//  if (Serial.available()){ 
//      
//    String in_char = Serial.readStringUntil('\n'); 
//    if (in_char.toInt() > 500) {
//      digitalWrite(LED_BUILTIN, HIGH);
//    }
//    else {
//      digitalWrite(LED_BUILTIN, LOW);
//    }
//    
//    servo.write(in_char.toInt()); 
//    
//  }

  delay(50);
  
}
