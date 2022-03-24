import re

fWrite = open("ex.csv","w")
fRead = open("emd.csv","r")
firstLine = fRead.readline()

campo = r"([\w\d]+|\"[\d\w,]+\")((\{\d+\}|\{\d*,\d*\})(::\w+)?)?"
is_valid = r"^((" + campo + ")?[,;\n])+$"

validInfo = re.match(is_valid, firstLine)
lista = re.findall(campo, firstLine)

intervaloIndex = 0
indiceCampo = 0
intervaloFim = 0
soma = 0
secondLine = True


concatenate = ""
i=0

def sumArray(arr : list[str]) -> int:
    count = 0
    for v in arr:
        count += int(v)
    return count

fWrite.write("[")
if validInfo:
    for linha in fRead:
        linhaSplit = re.split(',', linha)
        posIN = []
        while i < (len(linhaSplit)):
            if re.search(r'\".*\"',linhaSplit[i]):
                posIN.append(linhaSplit[i])
            elif re.search(r'^\"',linhaSplit[i]):
                while linhaSplit[i][-1] != "\"":
                    concatenate = concatenate + linhaSplit[i]+ ","
                    i+=1
                concatenate = concatenate + linhaSplit[i]
                posIN.append(concatenate)
                concatenate = ""   
            else:
                posIN.append(linhaSplit[i])
            i+=1
        i=0    

        if secondLine:
            fWrite.write("\n  {\n")
        else:
            fWrite.write(",\n  {\n")   
    
        while(indiceCampo < len(lista)):
            valores = []
            
            if (intervaloVal := re.search(r'(?:\{(\d*),(\d*)\})',lista[indiceCampo][2])):                 #caso seja um array com intervalo de valores
    
                intervaloFim = int(intervaloVal.groups()[1]) + intervaloIndex                           #valor onde termina a escrita dos valores do array
                    #por exemplo se o array for {3,5} isto faz o intervaloIndex avançar 3 posições para começar a escrever
                while intervaloFim > intervaloIndex:
    
                    if intervaloIndex >= len(posIN):
                        intervaloIndex = intervaloFim - 1

                    elif (posIN[intervaloIndex] == "") or (posIN[intervaloIndex] == "\n"):   
                        intervaloIndex = intervaloFim - 1 
                        
                    elif intervaloIndex == intervaloFim-1:
                        valores.append(posIN[intervaloIndex])
                    
                    else:
                        valores.append(posIN[intervaloIndex])
                    intervaloIndex = intervaloIndex + 1
    
                
                if lista[indiceCampo][3] == "::sum":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_sum\" : " + str(soma))
                
                elif lista[indiceCampo][3] == "::media":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_media\" : " + str(soma/len(valores)))
    
                else :
                    fWrite.write("\t\""+lista[indiceCampo][0]+"\" : "+ str(valores).replace("'","").replace("\\n",""))
                    
                indiceCampo = indiceCampo + 1  
    
            elif (intervaloVal := re.search(r'(?:\{(\d+)\})',lista[indiceCampo][2])):                    #caso seja um array normal
                intervaloFim = int(intervaloVal.groups()[0]) + intervaloIndex                           #valor onde termina a escrita dos valores do array
                    #por exemplo se o array for {3,5} isto faz o intervaloIndex avançar 3 posições para começar a escrever
                while intervaloFim > intervaloIndex:
                    
                    if intervaloIndex >= len(posIN):
                        intervaloIndex = intervaloFim - 1
                    
                    elif (posIN[intervaloIndex] == "") or (posIN[intervaloIndex] == "\n"):   
                        intervaloIndex = intervaloFim - 1 


                    elif intervaloIndex == intervaloFim-1:
                        valores.append(posIN[intervaloIndex])

                    else:
                        valores.append(posIN[intervaloIndex])
                    
                    intervaloIndex = intervaloIndex + 1
    
                if lista[indiceCampo][3] == "::sum":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_sum\" : " + str(soma))
                
                elif lista[indiceCampo][3] == "::media":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_media\" : " + str(soma/len(valores)))
    
                else :
                    fWrite.write("\t\""+lista[indiceCampo][0]+"\" : "+ str(valores).replace("'","").replace("\\n",""))
                    
                indiceCampo = indiceCampo + 1   
    
            
            else:
                posIN[intervaloIndex] = posIN[intervaloIndex].strip("\n")
                fWrite.write("\t\""+lista[indiceCampo][0]+"\" : \"" + posIN[intervaloIndex]+"\"")
                intervaloIndex = intervaloIndex + 1
                indiceCampo = indiceCampo + 1
        
            if indiceCampo == len(lista):
                fWrite.write("\n")
            else:
                fWrite.write(",\n")
    
        intervaloIndex = 0
        indiceCampo = 0
        fWrite.write("  }")
        secondLine = False
    fWrite.write("\n]")
else:
    print("Erro na informacao do ficheiro")