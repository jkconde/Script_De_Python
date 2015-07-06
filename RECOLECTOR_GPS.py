#!/usr/bin/env python

import sys

galileo_path = "/media/mmcblk0p1/"

if galileo_path not in sys.path:
 sys.path.append(galileo_path)

from pyGalileo import *


onModulePin= 2


def setup():

  pinMode(onModulePin, OUTPUT);
  #Serial.begin(115200);    

  print("Starting...");
  power_on()

  delay(5000)

  # starts GPS session in stand alone mode
  answer = sendATcommand("AT+CGPS=1,1","OK",1000);    
  if (answer == 0):
  
    print("Error starting the GPS");
    print("The code stucks here!!");
    while(1);
  
def loop():

  answer = sendATcommand("AT+CGPSINFO","+CGPSINFO:",1000);    # request info from GPS
  if (answer == 1):
  

    counter = 0
    
    gps_data[counter] = read()
    counter++
    
    while(gps_data[counter - 1] != '\r'):
          gps_data[counter] = read()
          counter++
    gps_data[counter] = '\0'
    if(gps_data[0] == ',')
    
      print("No GPS data available") 
    
    else:
      print("GPS data:")
      print(gps_data)  
      print("")
           

  
  else:
    print("Error") 
  

  delay(5000)


def power_on():

  uint8_t answer=0;

  #checks if the module is started
  answer = sendATcommand("AT", "OK", 2000)
  if (answer == 0):
    # power on pulse
    digitalWrite(onModulePin,HIGH);
    delay(3000);
    digitalWrite(onModulePin,LOW);

    # waits for an answer from the module
    while(answer == 0){    
      # Send AT every two seconds and wait for the answer
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
      
    
    # Waits for the answer with time out
  
  while((answer == 0) && ((millis() - previous) < timeout));    

  return answer

if __name__ == "__main__":
    
    setup();
    while(1):
        loop();





































































































































