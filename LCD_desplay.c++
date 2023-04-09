#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
unsigned long startTime = 0;
unsigned long interval = 500;
unsigned long currentTime = 0;

void setup() {
   lcd.begin(16,2);
}

void loop() {
  currentTime = millis();
  if (currentTime - startTime >= interval) {
    startTime = currentTime;
    lcd.clear();
    lcd.print(currentTime);
  }
}
