from algoritmos_basicos import utilidades


def sort(array):
    sortList(0,len(array)-1)

def sortList(inf,sup):
    if sup-inf >= 1:
       medio1=(inf+sup)/2
       medio2=medio1+1
       sortList(inf,medio1)
       sortList(medio2,sup)
       combina(inf,mediog1,medio2,sup)

def combina(izq,medio1,medio2,derecho):
    indIzq=izq
    indDer=medio2
    indComb=izq
    combinado=[n]
    while indIzq<=medio1 and indDer<=derecho:
        if array[indIzq]<=array[indDer]:
            indComb+=1
            indIzq+=1
            combinado[indComb]=array[indIzq]
        else:
            indComb+=1
            indDer+=1
            combinado[indComb]=array[indDer]
    if(indIzq==medio2):        
        while indDer <= derecho:
            indComb+=1
            indDer+=1
            combinado[indComb]=array[indDer]
    else:
        while indIzq <= medio1:
            indComb+=1
            indIzq+=1
            combinad o[indComb]=array[indIzq]
    for i in range(izq,derecho+1):
        array[i]=combinado[i]
#INICIO DEL PROGRAMA
n=int(input("Limite del array: "))
array=[]
utilidades.leeLista(n, array, "Ingresa los elementos")
sort(array)
utilidades.muestraLista(array, "Los elementos ordenados son: ")
