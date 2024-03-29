import re

fWrite = open("output.json","w")                                                                                # abre ficheiro de escrita
fRead = open("input.csv","r")                                                                                   # abre ficheiro de leitura
firstLine = fRead.readline()                                                                                    # recolhe a primeira linha

campo = r"([\w]+|\"[\w,;|\s]+\")((\{\d+\}|\{\d*,\d+\})(::\w+)?)?"                                               # er para 1 campo
cabecalho = r"^((" + campo + ")?[,;|\n])+$"                                                                     # er para cabeçalho

validInfo = re.match(cabecalho, firstLine)                                                                      # guarda se cabecalho é valido
listaCabecalho = re.findall(campo, firstLine)                                                                   # guarda lista de match objects de cada campo
sizeListComa = len(re.split(r'\,', firstLine))                                                                  # número de campos separados por ,
sizeListSemiColon = len(re.split(r'\;', firstLine))  
sizeListBarra = len(re.split(r'\|', firstLine))                                                                 # número de campos separados por |
split = re.split(r'[,;|\n]', firstLine)

indCampo = 0                                                                                                    # indice que vai percorrer os campos de informação
indCabecalho = 0                                                                                                # indice que vai percorrer os campos cabecalho   
intervaloFim = 0                                                                                                # indice onde acaba o intervalo se existir
soma = 0                                                                                                        # guarda a soma quando função de soma
secondLine = True                                                                                               # flag para saber se é a primeira linha de informação


def sumArray(arr : list[str]) -> int:                                                                           # função de soma
    count = 0
    for v in arr:
        count += int(v)
    return count

def sortArray(valores):
    return valores.sort()

def limpaLinha(linhaSplit):
    listaLimpa = []  
    concatenate = ""                                                    # onde vai ser guardados campos que pertencem juntos
    i = 0

    while i < (len(linhaSplit)):                                        # enquanto os campos não acabarem
        if re.search(r'\".*\"',linhaSplit[i]):                          # se existirem 2 aspas no mesmo campo, o campo está correto                                             
            listaLimpa.append(linhaSplit[i])

        elif re.search(r'^\"',linhaSplit[i]):                           # se existir só 1 aspa no campo, o campo tem de ser completado
            while linhaSplit[i][-1] != "\"":                            # enquanto não aparecer um campo a acabar com 1 aspas o campo é adicionado à string com o delimitador correto
                if sizeListComa+1 == len(split):                        # se delimitador for ,
                    concatenate = concatenate + linhaSplit[i]+ ","
                elif sizeListSemiColon+1 == len(split):                 # se delimitador for ;
                    concatenate = concatenate + linhaSplit[i]+ ";"
                else:                                                   # se delimitador for |
                    concatenate = concatenate + linhaSplit[i]+ "|"
                i+=1
            concatenate = concatenate + linhaSplit[i]                   # quando encontrar as aspas que faltam adiciona à string sem delimitador 
            listaLimpa.append(concatenate[1:-1])                        # campo adicionado à lista limpa
            
        else:                                                           # se campo não tiver nenhuma aspas está correto
            listaLimpa.append(linhaSplit[i])
        i+=1

    return listaLimpa 

def cleanValores(valores):                                                                                      # Cria uma lista de strings sem '
    cleaned = []
    for valor in valores:
        cleaned.append(str(valor).replace("'",""))
    return cleaned

def myLength(e):                                                                                                # função utilizada no sort pelo comprimento de um elemento
    return len(e)

fWrite.write("[")   
if validInfo:                                                                                                   # se o cabeçalho é válido avança
    for linha in fRead:                                                                                         # ciclo para cada uma das linhas de conteudo
        linhaSplit = re.split(r'[,;|\n]', linha)                                                                # guardar lista de campos separados por , ou ; para ser limpa
        listaLimpa = limpaLinha(linhaSplit)                                                                     # lista com correta posição de delimitadores (delimitadores dentro de strigs não contam como campo)
        
        if secondLine:                                                                                          # adiciona formato do JSON inicial
            fWrite.write("\n  {\n")
        else:                                                                                                   # adiciona formato JSON restante
            fWrite.write(",\n  {\n")   
    
        while(indCabecalho < len(listaCabecalho)):                                                              # enquanto os campos não acabarem
            valores = []                                                                                        # guarda os valores das listas
            strings = []                                                                                        # guarda as strings das listas
            listaTotal = []                                                                                     # guarda todo o conteudo da lista

            if intervaloVal := re.search(r'(?:\{(\d*),(\d+)\})|(?:\{(\d+)\})',listaCabecalho[indCabecalho][2]):     # se encontrar algum intervalo
            
                if (intervaloVal := re.search(r'(?:\{(\d*),(\d+)\})',listaCabecalho[indCabecalho][2])):             # se encontrar um intervalo variável
                    intervaloFim = int(intervaloVal.groups()[1]) + indCampo                                         # descobre o indice na linha de informação onde acaba o intervalo                          
                else:
                    intervaloVal = re.search(r'(?:\{(\d+)\})',listaCabecalho[indCabecalho][2])                      # se encontrar um intervalo fixo
                    intervaloFim = int(intervaloVal.groups()[0]) + indCampo                                         # descobre o indice na linha de informação onde acaba o intervalo 
                
                while intervaloFim > indCampo:                                                                      # Enquanto não chegar ao fim do intervalo:
    
                    if indCampo >= len(listaLimpa) or (listaLimpa[indCampo] == "") or (listaLimpa[indCampo] == "\n"):   # se for o último elemento do intervalo ou da linha indice avança
                        indCampo = intervaloFim - 1                                                                     # para o último valor do intervalo

                    elif re.search(r'\d+',listaLimpa[indCampo]):                                                        # se não for vazio e for um numero:
                        valores.append(listaLimpa[indCampo])                                                            # vai ser adicionado à lista dos valores
                        listaTotal.append(listaLimpa[indCampo])                                                         # vai ser adicionado à lista de todo o conteudo da lista
                    else:                                                                                               # se não for vazio e for uma string
                        strings.append("\""+listaLimpa[indCampo]+"\"")                                                  # vai ser adicionado à lista das strings
                        listaTotal.append("\""+listaLimpa[indCampo]+"\"")                                               # vai ser adicionado à lista de todo o conteudo da lista
                    
                    indCampo = indCampo + 1                                                                     

                
                if listaCabecalho[indCabecalho][3] == "::sum":                                                                      # se for uma função de soma
                    soma = sumArray(valores)                                                                                        # soma todos os valores guardados
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"_sum\" : " + str(soma))                                    # coloca no JSON com o prefixo _sum
                
                elif listaCabecalho[indCabecalho][3] == "::media":                                                                  # se for uma função de media 
                    soma = sumArray(valores)                                                                                        # soma todos os valores guardados
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"_media\" : " + str(soma/len(valores)))                     # coloca no JSON com o prefixo_media

                elif listaCabecalho[indCabecalho][3] == "::sort":                                                                   # se for uma função de sort           
                    cleaned = cleanValores(listaTotal)                                                                              # vai retirar ' de todos os valores
                    cleaned.sort()                                                                                                  # vai ordenar a lista de strings
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"_sort\" : " + str(cleaned).replace("\'",""))               
                
                elif listaCabecalho[indCabecalho][3] == "::sortByLength":                                                           # se for uma função de sortByLength                                 
                    cleaned = cleanValores(listaTotal)                                                                              # vai retirar ' de todos os valores
                    cleaned.sort(key=myLength)                                                                                      # vai ordenar a lista de strings pelo comprimento do valor       
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"_sortByLength\" : " + str(cleaned).replace("\'",""))

                else :
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"\" : "+ str(listaTotal).replace("'","").replace("\\n","")) # se for apenas para apresentar os números vai retirar primeiro os ' e o \n se existir
                    
                indCabecalho = indCabecalho + 1     
            
            else:
                listaLimpa[indCampo] = listaLimpa[indCampo].strip("\n")                                         # retira o \n do ultimo campo 
                if listaCabecalho[indCabecalho][0][0] != "\"":                                                  # verifica se cabecalho já tem ""
                    fWrite.write("\t\""+listaCabecalho[indCabecalho][0]+"\" : \"" + listaLimpa[indCampo]+"\"") 
                else:
                    fWrite.write("\t"+listaCabecalho[indCabecalho][0]+" : \"" + listaLimpa[indCampo]+"\"")      
                indCampo = indCampo + 1
                indCabecalho = indCabecalho + 1
        
            if indCabecalho == len(listaCabecalho):                                                          # se for o ultimo elemento da linha não vai colocar , depois dele
                fWrite.write("\n")
            else:                                                                                            # se nao for o ultimo elemento da linha vai colocar , depois dele
                fWrite.write(",\n")
    
        indCampo = 0
        indCabecalho = 0
        fWrite.write("  }")
        secondLine = False
    fWrite.write("\n]")
else:
    print("Erro na informacao do ficheiro")