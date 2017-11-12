ejercicio="""
Haz un algoritmo que, dada una frase cuente cuántas vocales,
digitos, espacios, palabras tiene"""
print(ejercicio)
frase=input("frase>>")
nVocal=0
nDigit=0
nEsp=0
pal=""
nPal=0
for i in frase:
    if i in 'aeiou':
        nVocal+=1
    elif i in '1234567890':
        nDigit+=1
    elif i == ' ':
        nEsp+=1
    if(i!=' '):
        pal=pal+i
    elif pal != '':
        nPal+=1
        pal=""
if pal!="":nPal+=1        
    

print("Numero de vocales: %d"%nVocal)
print("Numero de digitos: %d"%nDigit)
print("Numero de espacios: %d"%nEsp)
print("Numero de palabras: %d"%nPal)

    
