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
