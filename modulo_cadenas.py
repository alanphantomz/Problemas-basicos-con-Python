#devuelve las palabras de una cadena en forma de lista
def palabras(cad):
    pals=[]
    aux=""
    cad=cad+" "
    for i in range(len(cad)):
        if cad[i]!=' ':
            aux=aux+cad[i]
        else:
            pals.append(aux)
            aux=""
    return pals

#devuelve el mensaje secreto de una lista de palabras
def secretWord(lista):
    mensaje=""
    for i in range(len(lista)):
        mensaje=mensaje+lista[i][0]
    return mensaje
            
#contar caracteres en una cadena
def cuentaChr(cad,char):
    number=0
    for i in range(len(cad)):
        if cad[i]==char:
            number+=1
    return number

#invierte cadena
def invierte(cad):
    invertido=""
    for i in range(len(cad)):
        invertido=cad[i]+invertido
    return invertido

#Reemplaza un char en una cadena
def reemplaze(cad,charToReemp,char):
    cadNew=""
    for i in range(len(cad)):
        if cad[i] == charToReemp:
            cadNew+=char
        else:
            cadNew+=cad[i]
    return cadNew

#El cifrado de cesar
def cifradoCesar(message):
    cMessage=""
    for i in range(len(message)):
        numberCode=ord(message[i])+3
        cMessage+=chr(numberCode)
    return cMessage

def desCifradoCesar(message):
    eMessage=""
    for i in range(len(message)):
        numberCode=ord(message[i])-3
        eMessage+=chr(numberCode)
    return eMessage
