#!/usr/bin/env python

#import rospy
import sys
import time
import serial
#from std_msgs.msg import String

arduino = serial.Serial('/dev/ttyACM0', 115200,timeout = 1)
time.sleep(2)

cm = 391
Delay = "G07\n"
Home = "M18\n"
Up = "G05\n"
Down = "G06\n"
Length = 3*cm

def Centre(pos):
    if pos == '1':
        Command =  "G00 " + "X"+str(2*cm) + " Y"+str(-9*cm) +"\n"+Delay
    elif pos == '2':
        Command =  "G00 " + "X"+str(2*cm) + " Y"+str(-14*cm) +"\n"+ Delay
    elif pos == '3':
        Command =  "G00 " + "X"+str(5*cm) + " Y"+str(-9*cm) +"\n"+ Delay
    elif pos == '4':
        Command =  "G00 " + "X"+str(5*cm) + " Y"+str(-14*cm) +"\n"+ Delay
    return(Command)

def  X(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(0)+"\n"
    return(Command)
def  Y(Size):
    Command =  "G00 " + "X"+str(0) + " Y"+str(Size)+"\n"
    return(Command)

def  DiagTL(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(-Size)+"\n"
    return(Command)
def  DiagTR(Size):
    Command =  "G00 " + "X"+str(-Size) + " Y"+str(-Size)+"\n"
    return(Command)
def  DiagBL(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(Size)+"\n"
    return(Command)
def  DiagBR(Size):
    Command =  "G00 " + "X"+str(-Size) + " Y"+str(Size)+"\n"
    return(Command)

def DrawPentagon(pos):
    startpos = Centre(pos)
    
    serialprint(Home)
    time.sleep(10)
    serialprint(startpos)
    time.sleep(5)
    serialprint(Y(-Length/2))
    time.sleep(5)
    serialprint(DiagTL(Length/2))
    time.sleep(5)
    serialprint(DiagBL(Length/2))
    time.sleep(5)
    serialprint(Y(Length/2))
    time.sleep(5)
    serialprint(X(-Length))
    
def DrawSquare(pos):
    startpos = Centre(pos)
    
    serialprint(Home)
    time.sleep(10)
    serialprint(startpos)
    time.sleep(5)
    serialprint(X(Length))
    time.sleep(5)
    serialprint(Y(-Length))
    time.sleep(5)
    serialprint(X(-Length))
    time.sleep(5)
    serialprint(Y(Length))
    time.sleep(5)
   
def DrawDiamond(pos):
    startpos = Centre(pos)
    
    serialprint(Home)
    time.sleep(10)
    serialprint(startpos)
    time.sleep(5)
    serialprint(DiagTL(Length/2))
    time.sleep(5)
    serialprint(DiagBL(Length/2))
    time.sleep(5)
    serialprint(DiagBR(Length/2))
    time.sleep(5)
    serialprint(DiagTR(Length/2))
    time.sleep(5)
    
def DrawTriangle(pos):
    startpos = Centre(pos)
    
    serialprint(Home)
    time.sleep(10)
    serialprint(Up)
    serialprint(startpos)
    time.sleep(5)
    serialprint(Down)
    time.sleep(1)
    serialprint(DiagTL(Length/2))
    serialprint(Up)
    time.sleep(5)
    serialprint(Down)
    time.sleep(1)
    serialprint(DiagBL(Length/2))
    serialprint(Up)
    time.sleep(5)
    serialprint(Down)
    time.sleep(1)
    serialprint(Delay+X(-Length))
    serialprint(Up)
    time.sleep(5)

def serialprint(data):
    print(data)
    arduino.write(data)
    
def Gcoder(shape,pos):
    if shape == 'P':
        DrawPentagon(pos)
    if shape == 'S':
        DrawSquare(pos)
    if shape == 'D':
        DrawDiamond(pos)
    if shape == 'T':
        DrawTriangle(pos)
    
#def listener():
   # rospy.init_node('ProcessingNode' , anonymous=True)
   #rospy.Subscriber("processing", String, Gcoder)
   # rospy.spin()
    
if __name__ == '__main__':
    shape = list()
    pos = list()
    for x in range(0,4):
        shape.append(raw_input("Shape (P,T,S,D)? ")) 
        pos.append( raw_input("Position (1,2,3,4,0)? "))
        Gcoder(shape[x],pos[x])
    serialprint(Home)
