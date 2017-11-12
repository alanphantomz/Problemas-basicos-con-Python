def llenaLista(n):
    print("Ingrese uno a uno los elementos del vector:")
    v=[]
    for i in range(n):
        v.append(int(input("v[%d]:"%i)))
    return v

def mostrarLista(lista):
    for i in range(len(lista)):
        print("[%d]"%lista[i],end="")
    return
        
#nicia el programa
print("Dado un vector de n elementos, hacer rotar k elementos hacia la derecha")
n=int(input("n:"))
k=int(input("k:"))
v=llenaLista(n)
print("Lista ingresada: ",end="")
mostrarLista(v)
for i in range(k):
    aux=v[n-1]
    j=n-2
    while j>-1:
        v[j+1]=v[j]
        j-=1
    v[0]=aux
    
print("\nEl resultado es: ",end="")
mostrarLista(v)
