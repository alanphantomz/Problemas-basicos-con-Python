import math
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


print("Dado un vector de n elementos, formar un numero cada 2 elementos y llevarlos a otro vector")
n=int(input("n:"))
v=llenaLista(n)
neo=0
nv=[]
for i in range(0,n//2+n%2):
    if i<(n//2):
        neo=v[i*2]*10**(math.log10(v[i*2+1])+1)+v[i*2+1]
        nv.append(neo)
    else:
        nv.append(v[n-1])
print("El nuevo vector formado es: ")
mostrarLista(nv)
