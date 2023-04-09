#include <Servo.h> 
Servo myServo;
int button = 2;
int green = 9;
int red = 10;
int count = 3;

void setup(){ 
  myServo.attach(5);
  pinMode(button, INPUT);
  myServo.write(0);
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
}
void loop(){
  if(digitalRead(button) == HIGH && count > 0){
  	digitalWrite(green, HIGH);
    delay(500);
    digitalWrite(green, LOW);
    delay(500);
    myServo.write(90);
    delay(1000);
    myServo.write(0);
    count--;
  }
  if(count == 0){
  digitalWrite(red,HIGH);
  }
}