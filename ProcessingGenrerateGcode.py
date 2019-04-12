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

def Centre:
    Command =  "G00 " + "X"+str(10*cm) + " Y"+str(-10*cm)
    return(Command)

def  X(Size):
    Command =  "G00 " + "X"+str(Size) + " Y"+str(0)
    return(Command)

def  Y(Size):
    Command =  "G00 " + "X"+str(0) + " Y"+str(-1*Size)
    return(Command)

def DrawSquare(Size):
    Length = size*cm
    Command =  Delay +X(Length) + "\n" +  Delay +Y(Length) +  "\n" + Delay +  X(-1*Length) + "\n" +  Delay  + Y(-1*Length) + "\n"
    return(Command)

def serialprint(data):
    print(data)
    arduino.write(data)
    time.sleep(0.5)
    
def Gcoder(shape,size):
    if shape == 'S':
        info = DrawSquare(size)
        
    serialprint(Home)
    time.sleep(2)
    serialprint(info)
    


#def listener():
    #rospy.init_node('ProcessingNode' , anonymous=True)
    #rospy.Subscriber("processing", String, serialprint)
    #rospy.spin()
    
if __name__ == '__main__':
    shape = 'S'
    size = 5
    Gcoder(shape,size)
