#Ejercicio 1
colores=("rojo","azul","verde")
notas=(4.2,3.8,5.0)
edades=(18,20,22,19)
print(colores)
print(notas)
print(edades)
#Ejercicio2
numero=(5)
numero2=(5,)

print(type(numero))
print(type(numero2))
#Ejercicio 3
frutas=("manzana","pera","mango","uva")
#Direccionar y visualizar  por la posición
print("")
print(frutas[0])
print(frutas[1])
print(frutas[3])
#Prueba de registros de indices
print(frutas[-1])
print("")

#Prueba de Tupla con For
dias=("lunes","martes","miercoles","Jueves","viernes")
print("")
for dia in dias:
    print("Día:", dia)
print("")    
#Ejercicio 4
    
numeros=(2,4,6,4,8,4)
print("")
print("Tamaño de la tuppla números: ",len(numeros))
print("Cuantos números 4 hay: ",numeros.count(4))
print("Cual es la posición del número 8: ",numeros.index(8))
print("")
#Ejercicio 5
estudiante=("Ana",18,4.5)
nombre,edad,promedio=estudiante
print("")
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Promedio: ",promedio)
print("")

#Ejercicio 6
estudiantes=(("Ana",4.5),
             ("Luis",3.8),
             ("María",4.9))
print("")
for nombre,nota in estudiantes:
    print(nombre,"tiene nota", nota)
print("")

#Ejercicio de Error

#colores=("rojo","azul","verde")
#colores[0]="amarillo"
print("")
#Ejercicio  de cambio de tupla a lista
colores=("rojo","azul","verde")

lista_colores=list(colores)
lista_colores[0]="amarillo"
colores=tuple(lista_colores)
print("")

print("")
#Ejercicio tupla notas
notas=(4.0,3.5,5.0,4.2)
suma= 0
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print("Promedio: ",promedio)
print("")

#Ejemplo de mayor a menor
temperaturas=(18,22,19,25,21)

mayor=temperaturas[0]
menor=temperaturas[0]

for temp in temperaturas:
    if temp>mayor:
        mayor=temp
    if temp<menor:
        menor=temp
        
print("Mayor: ",mayor)
print("Menor: ", menor)