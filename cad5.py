ejercicio="""Dada una cadena cambiar las palabras que empiezan con una voca a mayuscula,
Las palabras que empiezan por una consonante dividirlas si su longitud es par"""
print(ejercicio)
cad=input("cadena>>>")+" "  
pal=""
nCad=""
for i in cad:
    if i==' ':
        if pal!="":
            if pal[0] in "aeiou":                
                nCad=nCad+pal.upper()
            elif pal[0].isalpha():
                if len(pal)%2==0:
                    lonPal=int(len(pal))            
                    nCad=nCad+pal[0:lonPal//2]+" "+pal[lonPal//2:lonPal]
                else:
                    nCad=nCad+pal
            else:
                nCad=nCad+pal
            pal=""
            nCad+=i
        else:
            nCad=nCad+i
    else:
        pal=pal+i
print("La nueva cadena es: %s"%nCad)
            
                
