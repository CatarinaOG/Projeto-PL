from posixpath import split
import re
import sys

fWrite = open("ex.csv","w")
f = open("emd1.csv","r")
g = f.readline()

flag = True
header = r"([\w ]+)((\{\d+\}|\{\d+,\d+\})(::\w+)?)?"
is_valid = r"^((" + header + ")?,)+$"

res = re.match(is_valid, g)
lista = re.findall(header, g)

contador = 0
contadorCabeca = 0
contadorElemArray = 0

fWrite.write("[\n")
for linha in f:
    linhaSplit = linha.split(",")
    fWrite.write("  {\n")

    while(contadorCabeca< len(lista)):
        
        if (intervaloVal := re.search(r'(?:\{(.+),(.+)\})',lista[contadorCabeca][2])): #caso seja um array com intervalo de valores
            contadorElemArray = int(intervaloVal.groups()[1]) + contador #valor onde termina a escrita dos valores do array
            contador = contador + int(intervaloVal.groups()[0]) -1 #por exemplo se o array for {3,5} isto faz o contador avançar 3 posições para começar a escrever
            fWrite.write("     \""+lista[contadorCabeca][0]+"\" : [")
            while contadorElemArray > contador: #este while desenha o array de elementos dentro de []
                
                if(contadorElemArray-1 == contador or (flag:=linhaSplit[contador+1]== "")): #caso seja o ultimo elemento tira o \n e escreve ] em vez de , 
                    linhaSplit[contador] = linhaSplit[contador].strip('\n')
                    fWrite.write(linhaSplit[contador]+"]\n")
                    if flag: #caso existam arrays por exemplo 3,3,2,, e os valores são {3,5} mal ele enconte um espaço vazio ele faz logo ] e passa para o próximo elemento
                        contador = contadorElemArray-1
                
                else: #caso seja um elemento no meio do array dá print do valor com , à frente
                    fWrite.write(linhaSplit[contador]+",")    
                contador = contador + 1
            contadorCabeca = contadorCabeca + 1
        
        elif (intervaloVal := re.search(r'(?:\{(.+)\})',lista[contadorCabeca][2])):    #caso seja um array normal
            contadorElemArray = int(intervaloVal.groups()[0]) + contador
            fWrite.write("     \""+lista[contadorCabeca][0]+"\" : [")

            while contadorElemArray > contador: #?
                if(contadorElemArray-1 == contador or (flag:=linhaSplit[contador+1]== "")):
                    linhaSplit[contador] = linhaSplit[contador].strip('\n')
                    fWrite.write(linhaSplit[contador]+"]\n")
                    if flag: #caso existam arrays por exemplo 3,3,2,, e os valores são {3,5} mal ele enconte um espaço vazio ele faz logo ] e passa para o próximo elemento
                        contador = contadorElemArray-1

                else:
                    fWrite.write(linhaSplit[contador]+",")      
                contador = contador + 1
 
            contadorCabeca = contadorCabeca + 1
        
        else:
            fWrite.write("     \""+lista[contadorCabeca][0]+"\" : \"" + linhaSplit[contador].strip('\n')+"\",\n")
            contador = contador +1
            contadorCabeca = contadorCabeca + 1
    contador = 0
    contadorCabeca = 0
    fWrite.write("  },\n")      
fWrite.write("]")
