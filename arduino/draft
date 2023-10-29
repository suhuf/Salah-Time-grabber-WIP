#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int reply;

int i = 0;

void setup() {

  Serial.begin(9600); // Baud rate that needs to match python
 
}

void loop() {

String t_Fajr;

if (Serial.available() > 0){
String t_Fajr = Serial.readStringUntil();
Serial.println(t_Fajr);

Serial.print("Data is in: ");
lcd.clear();

lcd.print(t_Fajr);
delay(900);

lcd.clear();
delay(222);

}

else{
  
  lcd.clear();
  delay(222);
  lcd.print("NO DATA FOUND");
  Serial.println("No data, passing. ");
  delay(502);

}

if (i == 0){

  lcd.begin(16, 2);
  lcd.print("Salah times ");
  lcd.setCursor(0,1);
  delay(2000);
  
  i = i + 1;
  
  }


if (i == 1) {

  //lcd.clear();
  delay(100);
  lcd.setCursor(0, 0);
  lcd.print("Fajr: " + t_Fajr + "Dhuhr:  Asr:  Maghrib:  Isha: ");
  delay(400);
  for (int positionCounter = 0; positionCounter < 20; positionCounter ++) {
    delay(200);
    // scroll one position left:
    lcd.scrollDisplayLeft();
    // wait a bit:
    delay(200);
    
  }

  delay(200);

  i = i - 1;


}
  
}
