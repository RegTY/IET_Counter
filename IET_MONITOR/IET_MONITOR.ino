#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
String words;
String names;
void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {

  while (Serial.available()) {
    if (Serial.available() > 0) {
    lcd.clear();
    lcd.setCursor(0, 0);
    words = Serial.readStringUntil('\n');
    names = Serial.readStringUntil('\n');
    lcd.print("#Recruits :" + words);
    lcd.setCursor(0, 1);
    lcd.print(names);
    Serial.flush();

  }

  }

}
