#!/usr/bin/env python

import sys
from time import time
from time import sleep
import serial

galileo_path = "/media/mmcblk0p1/"

if galileo_path not in sys.path:
 sys.path.append(galileo_path)

from pyGalileo import *

onModulePin= 2

def setup():

  pinMode(onModulePin, OUTPUT);
  ser=serial.Serial('/dev/ttyS0',115200,
                    bytesize=8,parity='N',
                    stopbits=1,timeout=10)    

  print("Starting...");
  power_on()

  sleep(5)

  # starts GPS session in stand alone mode
  answer = sendATcommand("AT+CGPS=1,1","OK",1);    
  if (answer == 0):
  
    print("Error starting the GPS");
    print("The code stucks here!!");
    while(1);
  
def loop():

  answer = sendATcommand("A+CGPSINFO",
                         "+CGPSINFO:",1)#request info    from GPS
  if answer:
  

 #   counter = 0
    
    gps_data= ser.read(128)
#    counter++
    
    while(gps_data[-1] != '\r'):
          gps_data+=ser.read(128)
#          counter++
    gps_data+= '\0'
    if(gps_data[0] == ',')
    
      print("No GPS data available") 
    
    else:
      print("GPS data:")
      print(gps_data)  
      print("")
           

  
  else:
    print("Error") 
  

  sleep(5)


def power_on():

  answer=0;
  #checks if the module is started
  answer = sendATcommand("AT", "OK", 2)
  if (answer == 0):
    # power on pulse
    digitalWrite(onModulePin,HIGH);
    sleep(3);
    digitalWrite(onModulePin,LOW);

    # waits for an answer from the module
    while(answer == 0){    
      # Send AT every two seconds and wait for the answer
      answer = sendATcommand("AT", "OK", 2000)    

def sendATcommand(ATcommand, expected_answer1, timeout):

  x=0
  answer=0
  ATcommand+= "\r\n"
  ATcommand=ATcommand.encode()
  #  unsigned long previous;
  response = ''
  #memset(response, '\0', 100) # Initialize the string
  #sleep(100)
  sleep(1)

  while( ser.inwaiting() > 0):
   ser.read(128) # Clean the input buffer

  print(ATcommand) # Send the AT command 


    #x = 0
  previous = time()

  # this loop waits for the answer
      
  response+= ser.read(128)
      #x++
#check if the desired answer is in the response of the module
      #if (strstr(response, expected_answer1) != NULL):    
      
  answer = expected_answer1 in response
      
    
    # Waits for the answer with time out
  
  while not answer and (time()-previous) < timeout: 
   response+= ser.read(128)
   answer = expected_answer1 in response

 
  #&& ((millis() - previous) < timeout));    

  return answer

if __name__ == "__main__":
    
    setup();
    while(1):
        loop();


