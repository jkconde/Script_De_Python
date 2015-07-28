#!/usr/bin/env python

import sys
<<<<<<< HEAD
from time import time
from time import sleep
import serial
=======
>>>>>>> 595099555896caf19bc26460b0c323875e30db70

galileo_path = "/media/mmcblk0p1/"

if galileo_path not in sys.path:
 sys.path.append(galileo_path)

from pyGalileo import *

<<<<<<< HEAD
onModulePin= 2

def setup():

  pinMode(onModulePin, OUTPUT);
  ser=serial.Serial('/dev/ttyS0',115200,
                    bytesize=8,parity='N',
                    stopbits=1,timeout=10)    
=======

onModulePin= 2


def setup():

  pinMode(onModulePin, OUTPUT);
  #Serial.begin(115200);    
>>>>>>> 595099555896caf19bc26460b0c323875e30db70

  print("Starting...");
  power_on()

<<<<<<< HEAD
  sleep(5)

  # starts GPS session in stand alone mode
  answer = sendATcommand("AT+CGPS=1,1","OK",1);    
=======
  delay(5000)

  # starts GPS session in stand alone mode
  answer = sendATcommand("AT+CGPS=1,1","OK",1000);    
>>>>>>> 595099555896caf19bc26460b0c323875e30db70
  if (answer == 0):
  
    print("Error starting the GPS");
    print("The code stucks here!!");
    while(1);
  
def loop():

<<<<<<< HEAD
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
=======
  answer = sendATcommand("AT+CGPSINFO","+CGPSINFO:",1000);    # request info from GPS
  if (answer == 1):
  

    counter = 0
    
    gps_data[counter] = read()
    counter++
    
    while(gps_data[counter - 1] != '\r'):
          gps_data[counter] = read()
          counter++
    gps_data[counter] = '\0'
>>>>>>> 595099555896caf19bc26460b0c323875e30db70
    if(gps_data[0] == ',')
    
      print("No GPS data available") 
    
    else:
      print("GPS data:")
      print(gps_data)  
      print("")
           

  
  else:
    print("Error") 
  

<<<<<<< HEAD
  sleep(5)
=======
  delay(5000)
>>>>>>> 595099555896caf19bc26460b0c323875e30db70


def power_on():

<<<<<<< HEAD
  answer=0;
  #checks if the module is started
  answer = sendATcommand("AT", "OK", 2)
  if (answer == 0):
    # power on pulse
    digitalWrite(onModulePin,HIGH);
    sleep(3);
=======
  uint8_t answer=0;

  #checks if the module is started
  answer = sendATcommand("AT", "OK", 2000)
  if (answer == 0):
    # power on pulse
    digitalWrite(onModulePin,HIGH);
    delay(3000);
>>>>>>> 595099555896caf19bc26460b0c323875e30db70
    digitalWrite(onModulePin,LOW);

    # waits for an answer from the module
    while(answer == 0){    
      # Send AT every two seconds and wait for the answer
<<<<<<< HEAD
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
=======
      answer = sendATcommand("AT", "OK", 2000);    

def sendATcommand(ATcommand, expected_answer1, unsigned int timeout):

x=0,  answer=0;
#  unsigned long previous;

  memset(response, '\0', 100);    # Initialize the string

  delay(100);

  while( available() > 0) read();    # Clean the input buffer

  print(ATcommand);    # Send the AT command 


    x = 0;
  previous = millis()

  # this loop waits for the answer
      
      response[x] = read()
      x++;
      # check if the desired answer is in the response of the module
      if (strstr(response, expected_answer1) != NULL):    
      
        answer = 1;
>>>>>>> 595099555896caf19bc26460b0c323875e30db70
      
    
    # Waits for the answer with time out
  
<<<<<<< HEAD
  while not answer and (time()-previous) < timeout: 
   response+= ser.read(128)
   answer = expected_answer1 in response

 
  #&& ((millis() - previous) < timeout));    
=======
  while((answer == 0) && ((millis() - previous) < timeout));    
>>>>>>> 595099555896caf19bc26460b0c323875e30db70

  return answer

if __name__ == "__main__":
    
    setup();
    while(1):
        loop();


<<<<<<< HEAD
=======



































































































































>>>>>>> 595099555896caf19bc26460b0c323875e30db70
