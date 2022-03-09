import re
import sys


f = open("emd.csv","r")
g = f.readline()
h = ""
if(re.search(r',.*\{.+\},',g)): #caso existam arrays para trabalhar
    print("1")

elif(re.search(r',.*\{.+\}.+,',g)): #caso existam arrays com funções de agregação
    print("2")

else: #caso normal quando não existe arrays    
    campos = g.split(',')
    campos2 = campos[:-1]
    
    for linha2 in campos2:
        h = h + "(?:(?P<" + linha2 + ">.*),)"
    
    h = h + "(?:(?P<" + campos[len(campos)-1][:-1] + ">.*))" 
    
    for linha in f:
        maluno = re.search(h,linha)
        if maluno:
            dic = maluno.groupdict()
            print(dic.get("index",0))
        else:
            print("Invalido")    