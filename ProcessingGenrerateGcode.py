#!/usr/bin/env python

#import rospy
import sys
import time
import serial
#from std_msgs.msg import String

arduino = serial.Serial('COM18', 115200,timeout = 1)
time.sleep(2)

cm = 391
Delay = "G07\n"
Home = "M18\n"
Up = "G05\n"
Down = "G06\n"
Length = 3*cm

def Centre(pos):
    if pos == '1':
        Command =  "G00 " + "X"+str(6*cm) + " Y"+str(-6*cm) +"\n"+Delay
    elif pos == '2':
        Command =  "G00 " + "X"+str(6*cm) + " Y"+str(-10*cm) + Delay
    elif pos == '3':
        Command =  "G00 " + "X"+str(10*cm) + " Y"+str(-6*cm) + Delay
    elif pos == '4':
        Command =  "G00 " + "X"+str(10*cm) + " Y"+str(-10*cm) + Delay
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

def DrawSquare(pos):
    startpos = Centre(pos)
    
    serialprint(Home);
    time.sleep(10)
    serialprint(startpos)
    time.sleep(5)
    serialprint(X(Length))
    time.sleep(5)
    serialprint(Y(Length))
    time.sleep(5)
    serialprint(X(-Length))
    time.sleep(5)
    serialprint(Y(-Length))
    time.sleep(5)
   
def DrawDiamond(pos):
    startpos = Centre(pos)
    
    serialprint(Home);
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
    
    serialprint(Home);
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
    shape = raw_input("Shape (S,T,D)? ")
    pos = raw_input("Position (1,2,3,4)? ")
    Gcoder(shape,pos)
