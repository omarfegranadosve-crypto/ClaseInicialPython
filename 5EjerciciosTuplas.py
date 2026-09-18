#Ejercicio No1
Nombres=("Luis","Marcos","Juana","Liliana","Susana")

print("")
print("El primer nombre de la tupla es: ",Nombres[0])
print("El último nombre de la tupla es: ",Nombres[-1])
print("")
#Ejercicio no2
sum_num=(1,2,4,6,4,8,4)
suma=0
for num in sum_num:
    suma=suma+num
print("")
print("La suma de la tupla con numeros",sum_num )
print("es: ",suma)
print("")
#Ejercicio No3
notas=(1.0,3.0,5.0,4.2,2.5)
suma= 0
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print("")
print("El promedio de las notas, ",notas)
print("es: ",promedio)
print("")
#Ejercicio No4
permitido=("hola","seguro","asignación","permitidas","palabras")
ing=input("Por favor ingrese un palabra para validar si esta en las palabras permitidas")
val=False
for permi in permitido:
    if(permi==ing):
        val=True
    else:
        val= False 
print("")       
if(val==True):    
    print("La palabra ingresada,(",ing,") si esta ")
else:
     print("La palabra ingresada,(",ing,") si esta ")
print("")
#Ejercicio No5
edades=(18,22,19,25,21,10,2,5,3)

mayor=0

for may in edades:
    if may>18:
        mayor=mayor+1
        
print("la cantidad de personas Mayores a 18 son: ",mayor)

     
