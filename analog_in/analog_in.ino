#include <Servo.h> 
#include <Thermocouple.h>
#include <MAX6675_Thermocouple.h>

#define SCK_PIN1 9
#define CS_PIN1 10
#define SO_PIN1 11

#define SCK_PIN2 3
#define CS_PIN2 5
#define SO_PIN2 6

// input pins and values
int analogX = A0; 
int analogY = A1; 
//int k_tc1 = 3; 
//int k_tc2 = 4; 
//int k_tc3 = 5; 

Thermocouple* thermocouple1;
Thermocouple* thermocouple2;

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

  thermocouple1 = new MAX6675_Thermocouple(SCK_PIN1, CS_PIN1, SO_PIN1);
  thermocouple2 = new MAX6675_Thermocouple(SCK_PIN2, CS_PIN2, SO_PIN2);
  
  //Declaring LED pin as output
//  pinMode(k_tc1, INPUT);
//  pinMode(k_tc2, INPUT);
//  pinMode(k_tc3, INPUT);

  servo.attach(servoPin); 
  pinMode(servoPin, OUTPUT);

}
void loop() {
  //Reading from potentiometer
  inputX = analogRead(analogX);
  inputY = analogRead(analogY);
//  inputTC1 = digitalRead(k_tc1); 
//  inputTC2 = digitalRead(k_tc2); 
//  inputTC3 = digitalRead(k_tc3); 

  const double celsius1 = thermocouple1->readCelsius();
  const double celsius2 = thermocouple2->readCelsius();

  Serial.print(inputX); 
  Serial.print(','); 
  Serial.print(inputY); 
  Serial.print(','); 
  Serial.print(celsius1); 
  Serial.print(','); 
  Serial.print(celsius2); 
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

  delay(177);
  
}
