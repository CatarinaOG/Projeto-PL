import re

fWrite = open("ex.csv","w")
fRead = open("emd1.csv","r")
firstLine = fRead.readline()

emptyValue = True
campo = r"([\w ]+)((\{\d+\}|\{\d+,\d+\})(::\w+)?)?"
is_valid = r"^((" + campo + ")?,)+$"

validInfo = re.match(is_valid, firstLine)
lista = re.findall(campo, firstLine)

intervaloIndex = 0
indiceCampo = 0
intervaloFim = 0
soma = 0
secondLine = True

def sumArray(arr : list[str]) -> int:
    count = 0
    for v in arr:
        count += int(v)
    return count

fWrite.write("[")
if validInfo:
    for linha in fRead:
        linhaSplit = linha.split(",")
        if secondLine:
            fWrite.write("\n  {\n")
        else:
            fWrite.write(",\n  {\n")   
    
        while(indiceCampo < len(lista)):
            valores = []
            
            if (intervaloVal := re.search(r'(?:\{(\d+),(\d+)\})',lista[indiceCampo][2])):                 #caso seja um array com intervalo de valores
    
                intervaloFim = int(intervaloVal.groups()[1]) + intervaloIndex                           #valor onde termina a escrita dos valores do array
                       #por exemplo se o array for {3,5} isto faz o intervaloIndex avançar 3 posições para começar a escrever
                while intervaloFim > intervaloIndex:
    
                    if linhaSplit[intervaloIndex] == "" or linhaSplit[intervaloIndex] == "\n":
                        intervaloIndex = intervaloFim - 1
                        
                    elif intervaloIndex == intervaloFim-1:
                        linhaSplit[intervaloIndex] = linhaSplit[intervaloIndex].strip('\n')
                        valores.append(linhaSplit[intervaloIndex])
                    
                    else:
                        valores.append(linhaSplit[intervaloIndex])
                    intervaloIndex = intervaloIndex + 1
    
                
                if lista[indiceCampo][3] == "::sum":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_sum\" : " + str(soma)+"\n")
                
                elif lista[indiceCampo][3] == "::media":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_media\" : " + str(soma/len(valores))+"\n")
    
                else :
                    fWrite.write("\t\""+lista[indiceCampo][0]+"\" : "+ str(valores).replace("'","") + "\n")
                    
                indiceCampo = indiceCampo + 1  
    
            elif (intervaloVal := re.search(r'(?:\{(\d+)\})',lista[indiceCampo][2])):                    #caso seja um array normal
                intervaloFim = int(intervaloVal.groups()[0]) + intervaloIndex                           #valor onde termina a escrita dos valores do array
                       #por exemplo se o array for {3,5} isto faz o intervaloIndex avançar 3 posições para começar a escrever
                while intervaloFim > intervaloIndex:
    
                    if intervaloIndex == intervaloFim-1:
                        linhaSplit[intervaloIndex] = linhaSplit[intervaloIndex].strip('\n')
                        valores.append(linhaSplit[intervaloIndex])
                    
                    else:
                        valores.append(linhaSplit[intervaloIndex])
                    intervaloIndex = intervaloIndex + 1
    
                if lista[indiceCampo][3] == "::sum":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_sum\" : " + str(soma)+"\n")
                
                elif lista[indiceCampo][3] == "::media":
                    soma = sumArray(valores)
                    fWrite.write("\t\""+lista[indiceCampo][0]+"_media\" : " + str(soma/len(valores))+"\n")
    
                else :
                    fWrite.write("\t\""+lista[indiceCampo][0]+"\" : "+ str(valores).replace("'","") + "\n")
                    
                indiceCampo = indiceCampo + 1   
    
            
            else:
                fWrite.write("\t\""+lista[indiceCampo][0]+"\" : \"" + linhaSplit[intervaloIndex].strip('\n')+"\",\n")
                intervaloIndex = intervaloIndex +1
                indiceCampo = indiceCampo + 1
            
    
        intervaloIndex = 0
        indiceCampo = 0
        fWrite.write("  }")
        secondLine = False
    fWrite.write("\n]")
else:
    print("Erro na informacao do ficheiro")