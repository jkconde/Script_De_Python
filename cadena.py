from consumidorcinco import sendRaw
import time

def main():
  with open("datostres.txt") as archivo:
    cadenadedatos=""
    date=time.strftime('%d/%m/%Y %H:%M:%S')
    for linea in archivo:
      print(linea)

      cadenadedatos+=linea[0:-1]+";"
      #sel=linea.split()
      #n=0
      #for valor in sel:
       #print(valor)
        #n=n+1
        #coment="sensor "+str(n) 
    cadenadedatos=cadenadedatos[0:-1]
    print(cadenadedatos)
    
    print(date)
    sendRaw(date, 1, cadenadedatos, 2, 3, -73.45, 7.87)
                
                
            #print(sel)


main()
