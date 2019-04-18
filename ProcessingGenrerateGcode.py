#!/usr/bin/env python

#import rospy
import sys
import time
import serial
#from std_msgs.msg import String

arduino = serial.Serial('COM18', 9600,timeout = 1)
time.sleep(2)

cm = 391
Delay = "G07\n"
Home = "M18\n"

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
    Command =  "G00 " + "X"+str(Size) + " Y"+str(0)
    return(Command)
def  Y(Size):
    Command =  "G00 " + "X"+str(0) + " Y"+str(Size)
    return(Command)

def  DiagTL(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(-Size)
    return(Command)
def  DiagTR(Size):
    Command =  "G00 " + "X"+str(-Size) + " Y"+str(-Size)
    return(Command)
def  DiagBL(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(Size)
    return(Command)
def  DiagBR(Size):
    Command =  "G00 " + "X"+str(-Size) + " Y"+str(Size)
    return(Command)

def DrawSquare(pos):
    Length = 3*cm
    startpos = Centre(pos)
    Command =  Delay+startpos+X(Length)+"\n"+Delay+Y(Length)+"\n"+Delay+X(-Length)+"\n"+Delay+Y(-Length)+"\n"
    return(Command)
def DrawDiamond(pos):
    Length = 3*cm
    startpos = Centre(pos)
    Command =  Delay+startpos+DiagTL(Length/2)+"\n"+Delay+DiagBL(Length/2)+"\n"+Delay+DiagBR(Length/2)+"\n"+Delay+DiagTR(Length/2)+"\n"
    return(Command)
def DrawTriangle(pos):
    Length = 3*cm
    startpos = Centre(pos)
    Command =  Delay+startpos+Delay+DiagTL(Length)+"\n"+Delay+DiagBL(Length)+"\n"+Delay+X(-Length)+"\n"
    return(Command)

def serialprint(data):
    print(data)
    arduino.write(data)
    time.sleep(0.5)
    
def Gcoder(shape,pos):
    info = Home
    if shape == 'S':
        info = info +DrawSquare(pos)
    if shape == 'D':
        info = info +DrawDiamond(pos)
    if shape == 'T':
        info = info +DrawTriangle(pos)

    time.sleep(2)
    serialprint(info)
    
#def listener():
   # rospy.init_node('ProcessingNode' , anonymous=True)
   #rospy.Subscriber("processing", String, Gcoder)
   # rospy.spin()
    
if __name__ == '__main__':
    shape = 'D'
    pos = '1'
    Gcoder(shape,pos)
