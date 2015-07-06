from consumidorje import sendRaw
import time

def main():
    with open("datos.txt") as archivo:
        for linea in archivo:
            print(linea)
            
            sel=linea.split()
            for valor in sel:
		print(valor)
          	date=time.strftime('%d/%m/%Y %H:%M:%S')
                print(date)
           	sendRaw(date, 1, valor, 2, 3, -73.5674567, 7.1565126)
                
                
            #print(sel)


main()
