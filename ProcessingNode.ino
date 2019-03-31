 /*
  RB-Dfr-539 :: Dual Bipolar Stepper Motor Controller for Arduino
  http://www.robotshop.com/en/dual-bipolar-stepper-motor-controller-arduino.html
*/

/*
This sample code is for testing the 2 stepper motors 
The rotation velocity can be adjusted by the code switch 
Microcontroller: Arduino UNO  
*/

#include <Servo.h>

int Xdir = 5; // 7
int Xstep = 2; //6
int Ydir = 6;
int Ystep = 3;
int en=8;  //Motor enable pin
int xhome = 9;
int yhome = 10;

int xcount = 0;
int ycount = 0;

Servo pen;
void setup()
{
  Serial.begin(9600);
  pen.attach(11);
  pinMode(Xdir,OUTPUT);
  pinMode(Xstep,OUTPUT);
  pinMode(Ydir,OUTPUT);
  pinMode(Ystep,OUTPUT);
  pinMode(en,OUTPUT);

  digitalWrite(en,LOW);// Low Level Enable
  pinMode(xhome, INPUT);
  pen.write(90);
}

// Y limit = 9375 counts  1cm = 391 counts 
// X limit = 7700 counts

int cm = 391;
void loop()
{
    Home();
    delay(500);
    xMove(1,10*cm);
    delay(500);
    yMove(1,5*cm);
    delay(1000);
    xMove(1,5*cm);
    delay(500);
    yMove(1,5*cm);
    delay(500);
    xMove(0,5*cm);
    delay(500);
    yMove(0,5*cm);
    delay(500);
    Home();
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
    xDir(dir);
    while(xcount < steps)
    {
      digitalWrite(Xstep,LOW);
      delayMicroseconds(200);
      digitalWrite(Xstep,HIGH);
      delayMicroseconds(200);
      xcount++;
    }
}

int yMove(bool dir,int steps)
{
    ycount = 0;
    yDir(dir);
    while(ycount < steps)
    {
      digitalWrite(Ystep,LOW);
      delayMicroseconds(200);
      digitalWrite(Ystep,HIGH);
      delayMicroseconds(200);
      ycount++;
    }
}

void Home()
{
    int buttonState;
    xcount = 0;
    ycount = 0;
    
    xDir(0);
    yDir(0);
    
    buttonState = 0;
    while(buttonState != 1)
    {
      buttonState = digitalRead(xhome);
      digitalWrite(Xstep,HIGH);
      delayMicroseconds(200);
      digitalWrite(Xstep,LOW);
      delayMicroseconds(200);
    }
    
    buttonState = 0;
    while(buttonState != 1)
    {
      buttonState = digitalRead(yhome);
      digitalWrite(Ystep,HIGH);
      delayMicroseconds(200);
      digitalWrite(Ystep,LOW);
      delayMicroseconds(200);
    }
}

