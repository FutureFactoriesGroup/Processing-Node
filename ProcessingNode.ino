 /*
  RB-Dfr-539 :: Dual Bipolar Stepper Motor Controller for Arduino
  http://www.robotshop.com/en/dual-bipolar-stepper-motor-controller-arduino.html
*/

/*
This sample code is for testing the 2 stepper motors 
The rotation velocity can be adjusted by the code switch 
Microcontroller: Arduino UNO  
*/

int Xdir = 7;
int Xstep = 6;
int Ydir = 4;
int Ystep = 5;

int x = 1;
int y = 1;
void setup()
{
  pinMode(Xdir,OUTPUT);
  pinMode(Xstep,OUTPUT);
  pinMode(Ydir,OUTPUT);
  pinMode(Ystep,OUTPUT);
}

void loop()
{
   MoveX(5000,1);
   delay(100);
   x = 1;
   MoveX(5000,0);
   delay(100);
   x = 1;
}

void MoveX(int dist ,bool dir)
{
  while(x!=0)
  {
    delayMicroseconds(2);
    digitalWrite(Xdir,dir);
    for(int i = 0; i < dist; i++)
    {
      digitalWrite(Xstep,LOW);
      delayMicroseconds(2);
      digitalWrite(Xstep,HIGH);
      delay(1);
    }
    x = 0;
  }
}

void MoveY(int dist ,bool dir)
{
  while(y!=0)
  {
    delayMicroseconds(2);
    digitalWrite(Ydir,dir);
    for(int j = 0; j < dist; j++)
    {
      digitalWrite(Ystep,LOW);
      delayMicroseconds(2);
      digitalWrite(Ystep,HIGH);
      delay(1);
    }
    y = 0;
  }
}

