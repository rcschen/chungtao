
#include <Wire.h>

int speed_motor1 = 6;  
int speed_motor2 = 5;
int direction_motor1 = 8;
int direction_motor2 = 7;

void setup()
{

  for(int i=4;i<=7;i++)
  {  
    pinMode(i, OUTPUT);  
  }
  Wire.begin(4);                
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);           
}

void loop()
{
  delay(100);
  Serial.println(">>>>>>>");
}


void receiveEvent(int howMany)
{
    int pwm1 = Wire.read();
    Serial.print(pwm1); 
    char c = Wire.read();
    Serial.print(c);
  
    int dir1 = Wire.read();
    Serial.print(dir1); 
    c = Wire.read();
    Serial.print(c);
  
    int pwm2 = Wire.read();
    Serial.print(pwm2); 
    c = Wire.read();
    Serial.print(c);
  
    int dir2 = Wire.read();
    Serial.println(dir2);
   
  // Apply these commands to the robot motors
    send_motor_command(speed_motor1,direction_motor1,pwm1,dir1);
    send_motor_command(speed_motor2,direction_motor2,pwm2,dir2);
}

// Function to command a given motor of the robot
void send_motor_command(int speed_pin, int direction_pin, int pwm, boolean dir)
{
    Serial.print(pwm);
    Serial.print(",");
    Serial.print(dir);
    Serial.println("--------");
    analogWrite(speed_pin,pwm); // Set PWM control, 0 for stop, and 255 for maximum speed
    digitalWrite(direction_pin,dir);
}
