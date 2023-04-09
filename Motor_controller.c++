int speed1 = 9;
int motor1a = 6;
int motor1b = 7;
int potPin = 0;
int potValue = 0;
int button = 2;
int buttonState = 0;

void setup() {
  pinMode(speed1, OUTPUT);
  pinMode(motor1a, OUTPUT);
  pinMode(motor1b, OUTPUT);
  pinMode(potPin, INPUT);
  pinMode(button, INPUT);
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  Serial.begin(9600);

}

void loop() {
  potValue = analogRead(potPin);
  //Serial.println(potValue);
  potValue = map(potValue, 0, 1023, 0, 255);
  analogWrite(speed1, potValue);
  buttonState = digitalRead(button);
  if (buttonState == HIGH){
    if (digitalRead(motor1a) == HIGH){
    	digitalWrite(motor1a, LOW);
        digitalWrite(motor1b, HIGH);
    }
    else{
    	digitalWrite(motor1a, HIGH);
        digitalWrite(motor1b, LOW);
    }
  	delay(200);
  }
}