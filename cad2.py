ejercicio="""Introducir una frase por teclado contar
cuantas palabras empiezan con un determinado caracter
"""
print(ejercicio)
frase=input("frase>>")
char=input("caracter>>")
word=""
cIni=0
for i in frase:
    if i == ' ':
        if word!="":
            if word[0]==char:
                cIni+=1
            word=""
    else:
        word=word+i
print("%d palabras empiezan en %s"%(cIni,char))
        
