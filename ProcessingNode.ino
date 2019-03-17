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
int Xen=8;  //Motor X enable pin
int Yen=12;  //Motor Y enable pin

int button = 2;
int xcount = 0;
int ycount = 0;
void setup()
{
  Serial.begin(9600);
  pinMode(Xdir,OUTPUT);
  pinMode(Xstep,OUTPUT);
  pinMode(Ydir,OUTPUT);
  pinMode(Ystep,OUTPUT);
  pinMode(Xen,OUTPUT);
  pinMode(Yen,OUTPUT);
  digitalWrite(Xen,LOW);// Low Level Enable
  digitalWrite(Yen,LOW);// Low Level Enable

  pinMode(button,INPUT);
}
// Y limit = 1900 counts
// X limit = 2320 counts
void loop()
{
    xMove(1,700);
    delay(200);
    yMove(1,700);
    delay(200);
    xMove(0,700);
    delay(200);
    yMove(0,700);
    delay(200);
    while(1){}
}

int xDir(bool dir)
{
  digitalWrite(Xdir,dir);
}

int yDir(bool dir)
{
  digitalWrite(Ydir,dir);
}

int xMove(bool dir,int steps)
{
    xcount = 0;
    digitalWrite(Xen,LOW);// Low Level Enable
    digitalWrite(Yen,HIGH);// Low Level Disable
    xDir(dir);
    yDir(0);
    while(xcount < steps)
    {
      digitalWrite(Xstep,LOW);
      delayMicroseconds(10);
      digitalWrite(Xstep,HIGH);
      delay(1);
      xcount++;
    }
    digitalWrite(Xen,HIGH);// Low Level Enable
    digitalWrite(Yen,HIGH);// Low Level Enable
}

int yMove(bool dir,int steps)
{
    ycount = 0;
    digitalWrite(Yen,LOW);// Low Level Enable
    digitalWrite(Xen,HIGH);// Low Level Disable
    yDir(dir);
    xDir(0);
    while(ycount < steps)
    {
      digitalWrite(Ystep,LOW);
      delayMicroseconds(10);
      digitalWrite(Ystep,HIGH);
      delay(1);
      ycount++;
    }
    digitalWrite(Xen,HIGH);// Low Level Enable
    digitalWrite(Yen,HIGH);// Low Level Enable
}

