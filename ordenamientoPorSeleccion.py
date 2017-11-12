print ("wellcame ")
print ("Input size: ")
n=int(input(">"))
numbers=[]
print("Ahora ingrese los numeros sucesivos")
for i in range(n):
    numbers.append(int(input(str(i)+": ")))

for i in range(n):
    moreSmall=i
    for j in range(i+1,n):
        if(numbers[j]<numbers[moreSmall]):
            moreSmall=j
    aux=numbers[i]
    numbers[i]=numbers[moreSmall]
    numbers[moreSmall]=aux
print ("Ya ordenamos su array de numeros: ")    
print(numbers)

print(list(range(45)))
