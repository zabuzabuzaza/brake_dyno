//Initializing LED Pin
int led_pin1 = 11;
int led_pin2 = 10;
int led_pin3 = 9;
int led_pin4 = 6;

int analogX = A0; 
int analogY = A1; 

int inputX; 
int inputY; 
int led_value1; 
int led_value2; 
int led_value3; 
int led_value4; 

long start_time; 

void setup() {
  Serial.begin(9600); 
  digitalWrite(LED_BUILTIN, LOW); 
  //Declaring LED pin as output
  pinMode(led_pin1, OUTPUT);
  pinMode(led_pin2, OUTPUT);
  pinMode(led_pin3, OUTPUT);
  pinMode(led_pin4, OUTPUT);


}
void loop() {
  //Reading from potentiometer
  inputX = analogRead(analogX);
  inputY = analogRead(analogY);
  
  Serial.print(millis() - start_time);
  Serial.print(','); 
  Serial.print(inputX); 
  Serial.print(','); 
  Serial.print(inputY); 
  Serial.print('\n'); 


  if (Serial.available()){
    int inByte = Serial.read(); 
    if (inByte == '1') {
      digitalWrite(LED_BUILTIN, HIGH); 
    }
    else {
      digitalWrite(LED_BUILTIN, LOW); 
    }
  }
  //Mapping the Values between 0 to 255 because we can give output
  //from 0 -255 using the analogwrite funtion
  led_value1 = map(inputX, 0, 1023, 0, 150);
  led_value2 = map(inputX, 0, 1023, 150, 0);
  led_value3 = map(inputY, 0, 1023, 0, 150);
  led_value4 = map(inputY, 0, 1023, 150, 0);
  analogWrite(led_pin1, led_value1);
  analogWrite(led_pin2, led_value2);
  analogWrite(led_pin3, led_value3);
  analogWrite(led_pin4, led_value4);
  
  delay(50);
  
}
