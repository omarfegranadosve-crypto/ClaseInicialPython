#Ejercicio No1
Nombres=("Luis","Marcos","Juana","Liliana","Susana")

print("")
print("El primer nombre de la tupla es: ",Nombres[0])
print("El último nombre de la tupla es: ",Nombres[-1])
print("")
#----------------------------------------------------------------------------------------------#
#Ejercicio no2
sum_num=(1,2,4,6,4,8,4)
suma=0
for num in sum_num:
    suma=suma+num
print("")
print("La suma de la tupla con numeros",sum_num )
print("es: ",suma)
print("")
#----------------------------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------------------------#
#Ejercicio No4
palab=("hola","prueba","lista","palabra", "aceptada", "Sí", "No")
ing=input("por favor ingrese la palabra que se quiere validar si existe en la lista")
val=1
while val!=0:
  if ing in palab:
    print ("La palabra,(",ing,") se encuentra en la lista aceptada")
    val=0
  else:
    print ("La palabra,(",ing,") no se encuentra en la lista aceptada")
    val=1
    ing=input("por favor ingrese la palabra que se quiere validar si existe en la lista")
print("Gracias por usar el sistema de validación de palabras")
print("")
#----------------------------------------------------------------------------------------------#
#Ejercicio No5
edades=(18,22,19,25,21,10,2,5,3)

mayor=0

for may in edades:
    if may>18:
        mayor=mayor+1
        
print("la cantidad de personas Mayores a 18 son: ",mayor)

     
