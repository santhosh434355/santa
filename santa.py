#include <LiquidCrystal.h>

const int trigPin = 8;
const int echoPin = 9;
const int ledA = 13;
const int ledB = 12;
const int ledC = 11;
const int ledD = 10;
const int buzzerPin = 11;  // Pin connected to the positive terminal of the buzzer
const int max_distance = 1000;

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);  // RS, E, DB4, DB5, DB6, DB7

void setup() {
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);
  pinMode(ledD, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);  // Set the buzzer pin as an output
  
  lcd.begin(16, 2);  // Initialize the LCD
  lcd.print("Distance:");
}

void loop() {
  long duration, cm;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  cm = duration * 0.034 / 2; // Calculate distance in cm based on the speed of sound
  
  if (cm >= 0 && cm < max_distance) {
    lcd.setCursor(0, 1);  // Set cursor to the second line
    lcd.print("               ");  // Clear the previous distance value
    lcd.setCursor(0, 1);  // Set cursor to the second line
    
    lcd.print("Distance: ");
    lcd.print(cm);
    lcd.print(" cm");

    if (cm >= 181) {
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, LOW);
      digitalWrite(ledC, LOW);
      digitalWrite(ledD, LOW);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Safe Level......");
    } else if (cm >= 136 && cm <= 180) {
      digitalWrite(ledA, HIGH);
      digitalWrite(ledB, LOW);
      digitalWrite(ledC, LOW);
      digitalWrite(ledD, LOW);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Normal Level!");
    } else if (cm >= 91 && cm <= 135) {
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, HIGH);
      digitalWrite(ledC, LOW);
      digitalWrite(ledD, LOW);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Above Normal!!");
    } else if (cm >= 46 && cm <= 90) {
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, LOW);
      digitalWrite(ledC, HIGH);
      digitalWrite(ledD, LOW);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Warning Level!!!");
    } else if (cm >= 0 && cm <= 45) {
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, LOW);
      digitalWrite(ledC, LOW);
      digitalWrite(ledD, HIGH);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Red Alert!!!!");
      
      // Activate the buzzer
      digitalWrite(buzzerPin, HIGH);
    } else {
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, LOW);
      digitalWrite(ledC, LOW);
      digitalWrite(ledD, LOW);
      lcd.setCursor(0, 0);  // Set cursor to the first line
      lcd.print("Out of Range");
      
      // Deactivate the buzzer
      digitalWrite(buzzerPin, LOW);
    }
  } else {
    lcd.setCursor(0, 0);  // Set cursor to the first line
    lcd.print("Out of Range");
    lcd.setCursor(0, 1);  // Set cursor to the second line
    lcd.print("               ");  // Clear the previous distance value
    
    digitalWrite(ledA, LOW);
    digitalWrite(ledB, LOW);
    digitalWrite(ledC, LOW);
    digitalWrite(ledD, LOW);
    
    // Deactivate the buzzer
    digitalWrite(buzzerPin, LOW);
  }

  delay(100);
}
