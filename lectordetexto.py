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
       #sel=linea.split()
      # n=0
       #for valor in sel:
        # print(valor)
         #n=n+1
         #coment="sensor "+str(n) 
         #date=time.strftime('%d/%m/%Y %H:%M:%S')
     cadenadedatos=cadenadedatos[0:-1]
     print(cadenadedatos)
    
     print(date)
     sendRaw(date, 1, cadenadedatos, 2, 3, -73.45, 7.87)

         #sendRaw(date, 1, valor, 2, 3, -73.45, 7.87,coment)
     os.remove(datosarenas)               
                
            #print(sel)


main()
