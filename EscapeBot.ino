#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void forward(int time) {
  servoLeft.write(0);
  servoRight.write(180);
  delay(time);
}

void reverse(int time) {
  servoLeft.write(180);
  servoRight.write(0);
  delay(time);
}

void turnRight(int time) {
  servoLeft.write(180);
  servoRight.write(180);
  delay(time);
}

void turnLeft(int time) {
  servoLeft.write(0);
  servoRight.write(0);
  delay(time);
}

void stopRobot() {
  servoLeft.write(90);
  servoRight.write(90);
}

void setup(){                                 
  tone(4, 3000, 1000);                       
  delay(1000);                               
  servoLeft.attach(13);  
  servoRight.attach(12); 
  pinMode(10, INPUT);  pinMode(9, OUTPUT);   
  pinMode (3, INPUT); pinMode (2, OUTPUT);
  Serial.begin(9600);                        
}  

int irDetect(int irLedPin, int irReceiverPin, long frequency){
  tone(irLedPin, frequency, 8);              
  delay(1);                                  
  int ir = digitalRead(irReceiverPin);       
  delay(1);                                  
  return ir;                                 
}  

void loop() { 
  int irLeft = irDetect(9, 10, 38000);  
  int irRight = irDetect (2, 3, 38000);
  
  if (irLeft == 1 && irRight == 1){
    Serial.println("forward");
    forward(3);
  } else if (irLeft == 0 && irRight == 1){
    Serial.println("right");
    turnRight(50);
  } else if (irLeft == 1 && irRight == 0){
    Serial.println("left");
    turnLeft(50);
  }else if (irRight == 0 && irLeft == 0){
    Serial.println("back");
    reverse(3);
  }
}
