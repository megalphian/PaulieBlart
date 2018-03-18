#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

#include <MeOrion.h>

double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
MeDCMotor motor_9(9);
MeDCMotor motor_10(10);
MeUltrasonicSensor ultrasonic_3(3);

char mode;

void setup(){
    Serial.begin(9600);
}

void loop(){
    if((ultrasonic_3.distanceCm()) < (30)){
      Serial.println("Obstacle detected");
      motor_9.run(0);
      motor_10.run(-150);
      delay(2500);
      mode = '3';
      return;
    }
    if(Serial.available() > 0) {
      mode = Serial.read();
      Serial.println(mode);
    }
    
    switch(mode){
      case '0':
          motor_9.run(0);
          motor_10.run(0);
          break;
        case '1':
          motor_9.run(100);
          motor_10.run(0);
          break;
        case '2':
          motor_9.run(100);
          motor_10.run(-50);
          break;
        case '3':
          motor_9.run(100);
          motor_10.run(-100);
          break;
        case '4':
          motor_9.run(50);
          motor_10.run(-100);
          break;
        case '5':
          motor_9.run(0);
          motor_10.run(-100);
          break;
      default:
        mode = 0;
    }
    
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
    
}


