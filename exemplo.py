import re
import sys

fWrite = open("ex.csv","w")
f = open("emd1.csv","r")
g = f.readline()
h = ""
i = 0
primeiro = 0
segundo = 0

header = r"([\w ]+)((\{\d+\}|\{\d+,\d+\})(::\w+)?)?"
is_valid = r"^((" + header + ")?,)+$"

res = re.match(is_valid, g)
lista = re.findall(header, g)

if(re.search(r',.*\{.+\},',g)): #caso existam arrays para trabalhar
    lista[len(lista)-1][0][:-1] #tira o \n do ultimo elemento
    campos2 = lista[:-1]
    for linha2 in lista:
        i = 0

        if(linha2[2] == ''): #caso a informação não tenha {}
            h = h + "(?:(?P<" + linha2[0] + ">.*),)"

        elif(p := re.search("(?:\{(.+),(.+)\})",linha2[2])): #caso existam dois valores dentro de {}
           primeiro = int(p[1])
           segundo = int(p[2])
           while(i < segundo-1):
                h = h + "(?:(?P<"+linha2[0]+str(i)+">.*),)"  
                i = i+1
           h = h + "(?:(?P<"+linha2[0]+str(i)+">.*))" 

        elif(p := re.search("(?:\{(.+)\})",linha2[2])): #caso exista um valor dentro de {}
           primeiro = p[1]
           while(i< primeiro-1):
                h = h + "(?:(?P<"+linha2[0]+str(i)+">.+),)"
                i = i+1
           h = h + "(?:(?P<"+linha2[0]+str(i)+">.+))"

    for linha in f:   
        maluno = re.search(h,linha)
        
        if not maluno:
            print("Erro na criação de dicionário")

        else:
            dic = maluno.groupdict()
            print(dic) 



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
            
            
            for cam in lista[:-1]: # escreve toda a informação entre aspas
                fWrite.write("  \"" + cam[0] + "\" : \""+ dic.get(cam[0]) +"\"\n    ")
                
            fWrite.write("},\n")   

    fWrite.write("]")           
        
            