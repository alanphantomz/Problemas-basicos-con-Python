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

def rotaOneVecesRight(lista):
    n=len(lista)
    aux=lista[n-1]
    i=n-1
    while i>0:
        lista[i]=lista[i-1]
        i-=1
    lista[0]=aux
    return
        
    
#nicia el programa
print("Dado un vector de n elementos, hacer rotar k elementos hacia la derecha")
n=int(input("n:"))
k=int(input("k:"))
v=llenaLista(n)
print("Lista ingresada: ",end="")
mostrarLista(v)
for i in range(k):
    rotaOneVecesRight(v)
print("\nEl resultado es: ",end="")
mostrarLista(v)
