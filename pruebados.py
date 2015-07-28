<<<<<<< HEAD
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
 
=======
from consumidorje import sendRaw
import time

def main():
  with open("datosdos.txt") as archivo:
    for linea in archivo:
      print(linea)
      sel=linea.split()
      n=0
      for valor in sel:
        print(valor)
        n=n+1
        coment="sensor "+str(n) 
        date=time.strftime('%d/%m/%Y %H:%M:%S')
        sendRaw(date, 1, valor, 2, 3, -73.45, 7.87,coment)
                
                
            #print(sel)


main()
>>>>>>> 595099555896caf19bc26460b0c323875e30db70
