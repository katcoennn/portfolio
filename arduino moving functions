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

  void setup() {
    servoLeft.attach(13);  // Set left servo to digital pin 10
    servoRight.attach(12);  // Set right servo to digital pin 9
  }

void loop () {  
if (infrared sensor far away from something)
{
  forward(100);
}
else
{
  turnLeft();
}
}
