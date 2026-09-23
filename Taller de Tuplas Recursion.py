##Punto No 1
#Cree una tupla llamada lenguajes con cinco lenguajes de programación. Muestre la tupla completa,
#el primer elemento, el último elemento y la cantidad total de elementos usando len(). Nivel sugerido:
#Básico.
Lenguajes=("C#","Python","Julia","Java","C++")
print(Lenguajes)
print(Lenguajes[1])
print(Lenguajes[-1])
print("Punto No1")
print("La cantidad de elementos de la tupla es: ",len(Lenguajes))
print("")
#---------------------------------------------------------------
##Punto No 2
#Defina una tupla con las edades de 10 personas. Recorra la tupla e imprima únicamente las edades
#mayores o iguales a 18 años. Al final, muestre cuántas personas son mayores de edad. Nivel sugerido:
#Básico.
edades=(18,22,19,25,21,10,2,5,3,7)
mayor=0
for may in edades:
    if may>=18:
        mayor=mayor+1
print("Punto No2")        
print("la cantidad de personas Mayores o iguales a 18 son: ",mayor)
print("")
#-----------------------------------------------------------------
#Punto No3
#Cree una tupla con ocho números enteros. Calcule y muestre la suma, el valor mayor, el valor menor
#y el promedio de los datos. Puede usar sum(), max() y min(). Nivel sugerido: Básico.
num=(1,2,9,5,3,5,8,12)
may=0
men=1000
suma=0
for i in num:
    if i>may:
        may=i
for i in num:
    if i<men:
        men=i
for i in num:
    suma=i+suma
print("Punto No3")
print("Por medio de For")
print("El promedio de los números es", sum(num)/len(num))
print("La suma de los números de la tupla es: ", suma)
print("El número más grande de la tupla es: ",may)
print("El número más pequeño de la tupla es: ",men)
print("Usando comando Sum(), Max, Min")
print("El promedio de los números es", sum(num)/len(num))
print("La suma de los números de la tupla es: ", sum(num))
print("El número más grande de la tupla es: ",max(num))
print("El número más pequeño de la tupla es: ",min(num))
print("")

#-----------------------------------------------------------------
#Punto No4
#Solicite al usuario una palabra y cree una tupla con cada uno de sus caracteres. Muestre la tupla y
#determine cuántas veces aparece la letra a. Tenga en cuenta mayúsculas y minúsculas. Nivel sugerido:
#Básico.

pal=input("Por favor ingrese la palabra, para identificar cuantas a hay ")

