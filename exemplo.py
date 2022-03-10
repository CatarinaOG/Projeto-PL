import re
import sys

fWrite = open("ex.csv","w")
f = open("emd.csv","r")
g = f.readline()
h = ""

header = r"([\w ]+)((\{\d+\}|\{\d+,\d+\})(::\w+)?)?"
is_valid = r"^((" + header + ")?,)+$"

res = re.match(is_valid, g)
lista = re.findall(header, g)

if(re.search(r',.*\{.+\},',g)): #caso existam arrays para trabalhar
    print("1")

elif(re.search(r',.*\{.+\}.+,',g)): #caso existam arrays com funções de agregação
    print("2")

else: #caso normal quando não existe arrays    
    campos2 = lista[:-1]
    lista[len(lista)-1][0][:-1] #tira o \n do ultimo elemento
    for linha2 in campos2:
        h = h + "(?:(?P<" + linha2[0] + ">.*),)"
    h = h + "(?:(?P<" + lista[len(lista)-1][0] + ">.*))" 
    
    fWrite.write("[\n") 
    for linha in f:   
        maluno = re.search(h,linha)
        
        if not maluno:
            print("Erro na criação de dicionário")

        else:
            dic = maluno.groupdict()
            fWrite.write("    {\n   ")
            
            for cam in lista: # escreve toda a informação entre aspas
                fWrite.write("  \"" + cam[0] + "\" : \""+ dic.get(cam[0]) +"\"\n    ")
            
            fWrite.write("},\n")   

    fWrite.write("]")           
        
            