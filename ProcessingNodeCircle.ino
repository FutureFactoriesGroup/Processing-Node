int ix,iy,ixx,iyy,iyold,ixold, delayx;
float xf,yf,ixf,iyf,iyyf,ifl,directionx,directiony;

int Xdir = 5; // 7
int Xstep = 2; //6
int Ydir = 6;
int Ystep = 3;
int en=8;  //Motor enable pin
int xhome = 9;
int yhome = 10;

void setup()
{
  Serial.begin(9600);  
  pinMode(Xdir, OUTPUT);   
  pinMode(Xstep, OUTPUT); 
  pinMode(Ydir, OUTPUT);     
  pinMode(Ystep, OUTPUT);
  pinMode(en,OUTPUT);

  digitalWrite(en,LOW);// Low Level Enable
}

void loop()
{
  circle(36, 100, 500); // (360 section, 100ms delay. radius of 10000  step)
}

void movexy(float xf, float yf, int delaxy, int directionx, int directiony)
{  
   iyold=0;
   ixold=0;
   
   if(xf>=yf)
   {
      for(ifl=1; ifl<=(xf+1); ifl++)
      {
          iyf=ifl*(yf/xf);
          if(round(iyf)>iyold)
          {
            digitalWrite(Ydir, directiony);
            digitalWrite(Ystep, HIGH);
          }
          digitalWrite(Xdir, directionx);
          digitalWrite(Xstep, HIGH);
          delayMicroseconds(delaxy);
          if(round(iyf)>iyold)
          {
            digitalWrite(Ystep, LOW); 
            iyold=iyold+1;
          }  
          digitalWrite(Xstep, LOW); 
          delayMicroseconds(delaxy); 
       }
    }
  else
  {
     for(ifl=1; ifl<=(yf+1); ifl++)
     {
        ixf=ifl*(xf/yf);
        if(round(ixf)>ixold)
        {
          digitalWrite(Xdir, directionx);
          digitalWrite(Xstep, HIGH);
        }
        digitalWrite(Ydir, directiony);
        digitalWrite(Ystep, HIGH);
        delayMicroseconds(delaxy);
        if(round(ixf)>ixold)
        {
         digitalWrite(Xstep, LOW); 
         ixold=ixold+1;
        }  
        digitalWrite(Ystep, LOW); 
        delayMicroseconds(delaxy);   
      }
  }
}

void circle(int div,float delaycirc, float rad)
{  // (division(more=smooth), delay, radius)
  float xxold=0;
  float yyold=0;
  for(int idiv=0; idiv<=(div); idiv++)
  {
    float divfloat=idiv;
    float xx=(cos(2*PI/div*divfloat)-0)*rad; 
    int x=abs(xx-xxold); 
    xxold=xx;
    float yy=(sin(2*PI/div*divfloat)-0)*rad; 
    int y=abs(yy-yyold); 
    yyold=yy;
    
    if( xx<0)
    {
      directionx=0;
    }
    else
    {
      directionx=1;
    }
    if( yy<0)
    {
      directiony=0;
    }
      else
    {
      directiony=1;
    }
    movexy(x,y,delaycirc, directionx, directiony);
  }
  delay(1000);
}
