from algoritmos_basicos import utilidades


def sort(array):
    for siguiente in range(1,len(array)):
        insercion=array[siguiente]
        moverElemento=siguiente
        while moverElemento > 0 and array[moverElemento-1]>insercion:
            array[moverElemento]=array[moverElemento-1]
            moverElemento=moverElemento-1
        array[moverElemento]=insercion
        
#INICIO DEL PROGRAMA
n=int(input("Limite del array: "))
array=[]
utilidades.leeLista(n, array, "Ingresa los elementos")
sort(array)
utilidades.muestraLista(array, "Los elementos ordenados son: ")
