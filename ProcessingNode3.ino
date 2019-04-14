#include <Servo.h>

Servo punch;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
char serialInput;
int numPoints = 0;
int command[50] = {0};
int char2int[50] = {0};

void setup()
{
  Serial.begin(9600);
  punch.attach(9);  // attaches the servo on pin 9 to the servo object
  punch.write(0);
}

void loop() 
{
 while(Serial.available() > 0)
  {
     serialInput = Serial.read();
     if(serialInput == 'D')
     {
      char2int[numPoints] =  Serial.parseInt();
      command[numPoints] = char2int[numPoints];
      numPoints++;
     
      if (serialInput == '\n') 
      {
        for(int x = 0;x < numPoints; x++)
        {
          Serial.println(command[x]); 
          if(command[1] == 100 )
          {
            punch.write(90);
            delay(500);
            punch.write(0);
          }
        }
        *char2int = 0;
        *Path = {0};
        numPoints = 0;
      }
    }
  }
}

