from modulo_vec import llenarLista
from modulo_vec import mostrarLista
ejercicio="Hacer leer un vector de n elementos\n" \
          "determinar cuantos numeros primos hay\n" \
          "en el vector, desplegar el contador de primos"
print(ejercicio)
n=int(input("n: "))
lista=llenarLista(n,"Ingrese elementos: ")
mostrarLista(lista,"Elementos ingresados: ")
listaPrimos=[]
contPrimos=0
for i in lista:
    contTemp = 0
    for j in range(1,i+1):
        if i%j==0:
            contTemp+=1
    if contTemp==2:
        contPrimos+=1
        listaPrimos.append(i)
print("Numero de primos: %d"%contPrimos)
mostrarLista(listaPrimos,"Estos son los primos: ")
