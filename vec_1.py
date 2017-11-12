def mostrarLista(lista):
    #muestra los elementos de un vector de enteros
    for i in range(len(lista)):
        print("[%d]"%lista[i],end="")
    return
    

#Inicia el programa
print("Dado un vector de tamaño n, llenar dicho\
 vector de la sgte forma: [2][4][6][4][6][8][6][8][10]...")
n=int(input("ingrese n:"))
v=[];c=0;j=0
for i in range(n):
    if j<3:
        c=c+2
        j=j+1
    else:
        j=1
        c=c-2
    v.append(c)
print("El vector obtenido es:")
mostrarLista(v)

