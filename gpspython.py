#!/usr/bin/env python
import sys
import serial

galileo_path = "/media/mmcblk0p1/";
if galileo_path not in sys.path:
    sys.path.append(galileo_path);

from pyGalileo import *


def setup()  

  pinMode(2, OUTPUT);    
  digitalWrite(2, HIGH);  
  #Serial.begin(57600);  
  #Serial.println("Enter AT commands:");  
  print("Introduzca Comandos AT");
  delay(500);
  #Serial1.begin(115200);  
  
def loop()  
   
  if (Serial1.available())  
    Serial.write(Serial1.read());  
  
    
  if (Serial.available())  
    Serial1.write(Serial.read());  
 
