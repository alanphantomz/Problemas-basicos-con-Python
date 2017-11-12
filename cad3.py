ejercicio="""input: hola mundo output: aloh odnum"""
print(ejercicio)
frase=input("frase>>")+" "
nFrase=""
pal=""
for i in frase:
    if i == ' ':
        if pal!="":
            nFrase=nFrase+pal+" "
            pal=""
    else :
        pal=i+pal
print(nFrase)
