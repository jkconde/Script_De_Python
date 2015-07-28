import glob
import os
import sys
from consumidorcinco import sendRaw
import time
#carpetaarenas='/home/root/sprintseis'
carpetaarenas='/home/radiogis/Descargas/Python-3.4.3/carpetaarenas'
sys.path.append(carpetaarenas)
def main():
  for datosarenas in glob.glob(os.path.join('*.txt')):
   with open(datosarenas) as archivo:
     cadenadedatos=""
     date=time.strftime('%d/%m/%Y %H:%M:%S')
     for linea in archivo:
       print(linea)
       cadenadedatos+=linea[0:-1]+";"
       
     cadenadedatos=cadenadedatos[0:-1]
     print(cadenadedatos)
    
     print(date)
     sendRaw(date, 1, cadenadedatos, 2, 3, -73.45, 7.87, 3)

         
     os.remove(datosarenas)               
                
            


main()
