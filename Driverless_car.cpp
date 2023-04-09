// Set a sonar in Pins 2 & 3 and create variables to measure distance
// Set an LED as output in Pin 9 and a button as input in Pin 4
// Set directional motor inputs in Pins 6 & 7 and a speed input in Pin 11
// Set a variable to check if the brake is hit as 0
int echoPin = 2;
int trigPin = 3;
int motor1a = 6;
int motor1b = 7;
int speed = 11;
int red = 9;
int button = 4;
float duration = 0.0;  // time for pulse to return back to sensor
float distance = 0.0;  // distance calculated using duration value
bool brake = false;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(speed, OUTPUT);
  pinMode(motor1a, OUTPUT);
  pinMode(motor1b, OUTPUT);
  pinMode(button, INPUT);
  pinMode(red, OUTPUT);
  digitalWrite(motor1a, HIGH);
}

// This function returns the distance as measured by the sonar sensor.
float checkDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) * 0.0344;
  return distance;
}

void loop() {
  if (digitalRead(button) == HIGH) {
    digitalWrite(motor1a, LOW);
    digitalWrite(red, HIGH);

    while (digitalRead(button) == HIGH) {}
    digitalWrite(motor1a, HIGH);
    digitalWrite(red, LOW);
  }

  distance = checkDistance();
  if (0 < distance && distance < 10) {
    // If an object is detected closer than 10cm, turn the motor on at a speed of 100 and blink the LED on and off for a quarter second each.
    analogWrite(speed, 100);
    if (digitalRead(red) == HIGH) {digitalWrite(red, LOW); delay(250);}
    else {digitalWrite(red, HIGH); delay(250);}
  }
  else if (10 <= distance && distance < 20) {
    // If an object is detected 10-20cm away, turn the motor on at a speed of 150 and blink the LED on and off for a half second each.
    analogWrite(speed, 150);
    if (digitalRead(red) == HIGH) {digitalWrite(red, LOW); delay(500);}
    else {digitalWrite(red, HIGH); delay(500);}
  }
  else if (distance > 20) {
    // If an object is detected 20cm or farther from the ultrasonic range finder, turn the motor on at a speed of 250.
    digitalWrite(red, LOW);
    analogWrite(speed, 250);
  }
}